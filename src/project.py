from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(self, artifact: Artifact) -> None:
        self.artifact = artifact
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class ArtifactBST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False
            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self) -> list[int]:
        result: list[int] = []

        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.artifact.artifact_id)
                dfs(node.right)

        dfs(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        result: list[int] = []

        def dfs(node):
            if node:
                result.append(node.artifact.artifact_id)
                dfs(node.left)
                dfs(node.right)

        dfs(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        result: list[int] = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.artifact.artifact_id)

        dfs(self.root)
        return result


class RestorationQueue:
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        if not self._items:
            return None
        return self._items.popleft()

    def peek_next_request(self) -> RestorationRequest | None:
        if not self._items:
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        if not self._items:
            return None
        return self._items.pop()

    def peek_last_action(self) -> str | None:
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name: str) -> None:
        self.stop_name = stop_name
        self.next: ExhibitNode | None = None


class ExhibitRoute:
    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new = ExhibitNode(stop_name)
        if not self.head:
            self.head = new
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def remove_stop(self, stop_name: str) -> bool:
        cur = self.head
        prev = None

        while cur:
            if cur.stop_name == stop_name:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next

        return False

    def list_stops(self) -> list[str]:
        result = []
        cur = self.head
        while cur:
            result.append(cur.stop_name)
            cur = cur.next
        return result

    def count_stops(self) -> int:
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for a in artifacts:
        counts[a.category] = counts.get(a.category, 0) + 1
    return counts


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {a.room for a in artifacts}


def sort_artifacts_by_age(
    artifacts: list[Artifact], descending: bool = False
) -> list[Artifact]:
    return sorted(artifacts, key=lambda a: a.age, reverse=descending)


def linear_search_by_name(
    artifacts: list[Artifact], name: str
) -> Artifact | None:
    for a in artifacts:
        if a.name == name:
            return a
    return None


def demo_museum_night() -> None:
    print("Moonlight Museum After Dark")

    artifacts = [
        Artifact(40, "Cursed Mirror", "mirror", 220, "North Hall"),
        Artifact(20, "Clockwork Bird", "machine", 80, "Workshop"),
        Artifact(60, "Whispering Map", "paper", 140, "Archive"),
        Artifact(10, "Glowing Key", "metal", 35, "Vault"),
        Artifact(30, "Moon Dial", "device", 120, "North Hall"),
        Artifact(50, "Silver Mask", "costume", 160, "Gallery"),
        Artifact(70, "Lantern Jar", "glass", 60, "Gallery"),
        Artifact(25, "Ink Compass", "device", 120, "Archive"),
    ]

    bst = ArtifactBST()
    for a in artifacts:
        bst.insert(a)

    print("Inorder IDs:", bst.inorder_ids())

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(40, "Polish cracked frame"))
    print("Next restoration request:", queue.peek_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added artifact")
    print("Undo action:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Mirror Room")
    print("Exhibit route:", route.list_stops())

    print("Category counts:", count_artifacts_by_category(artifacts))