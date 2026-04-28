# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Moonlight Coders
- Members: (add your names)
- Repository name: (your repo name)

---

## Project summary

Our project builds a system for organizing strange museum artifacts after dark. It uses multiple data structures like a binary search tree, queue, stack, and linked list to manage artifacts, restoration requests, routes, and reports. The system allows efficient searching, processing, and tracking of museum operations.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150–250 words)

We used a Binary Search Tree (BST) to store artifacts because it allows efficient searching, insertion, and traversal based on artifact IDs. Since each artifact has a unique ID, the BST structure makes it easy to quickly locate specific artifacts.

A queue was used for restoration requests because requests must be processed in the order they arrive (FIFO). This ensures fairness and correct processing order.

A stack was used for undo actions because the most recent action should be undone first (LIFO). This matches real-world undo behavior.

A singly linked list was used for the exhibit route because it allows easy insertion and removal of stops without shifting elements like in arrays. It also represents a natural sequence of stops.

The system is organized into separate classes for each data structure, making the code clean and modular. Helper functions handle reporting tasks like counting categories, sorting artifacts, and searching by name. This separation makes the system easier to understand and maintain.

---

## Complexity reasoning

- `ArtifactBST.insert`: O(h), where h is tree height, because it follows one path down the tree.
- `ArtifactBST.search_by_id`: O(h), same reason as insert.
- `ArtifactBST.inorder_ids`: O(n), because it visits all nodes.
- `RestorationQueue.process_next_request`: O(1), deque pop from front is constant time.
- `ArchiveUndoStack.undo_last_action`: O(1), list pop from end is constant time.
- `ExhibitRoute.remove_stop`: O(n), may need to traverse entire list.
- `sort_artifacts_by_age`: O(n log n), due to sorting.
- `linear_search_by_name`: O(n), checks each element.

---

## Edge-case checklist

### BST
- [x] insert into empty tree → handled by setting root
- [x] search for missing ID → returns None
- [x] empty traversals → returns empty list
- [x] duplicate ID → returns False and not inserted

### Queue
- [x] process empty queue → returns None
- [x] peek empty queue → returns None

### Stack
- [x] undo empty stack → returns None
- [x] peek empty stack → returns None

### Exhibit route linked list
- [x] empty route → works correctly
- [x] remove missing stop → returns False
- [x] remove first stop → updates head
- [x] remove middle stop → links previous to next
- [x] remove last stop → sets last.next to None
- [x] one-stop route → removal works

### Reports
- [x] empty artifact list → returns empty results
- [x] repeated categories → counted correctly
- [x] repeated rooms → stored once in set
- [x] missing artifact name → returns None
- [x] same-age artifacts → sorted correctly

---

## Demo plan / how to run

Run tests:
```bash
pytest -q