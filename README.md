# Social Network Graph System

## Overview

This project implements a graph-based social network system using adjacency lists and breadth-first search (BFS).

The system models user relationships as a graph and supports:

- First-degree connection retrieval
- Second-degree connection retrieval (via BFS)
- Third-degree connection retrieval (via BFS)
- Interest-based friend recommendations
- Time and space complexity analysis

This project demonstrates core data structures and algorithmic design principles from Data Structures & Algorithms.

---

## System Design

The social network is represented as:

- **Adjacency List (Dictionary of Dictionaries)**  
  - Keys: User IDs  
  - Values: Connected users (weighted edges)

Additional dictionaries store user attributes:

- Hobbies
- Music preferences
- Movie preferences

Edges can be weighted based on shared interests.

---

## Implemented Algorithms

### 1. First-Degree Connections

Direct lookup from adjacency list.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

### 2. Second-Degree Connections

Implemented using Breadth-First Search (BFS) with a queue and visited set.

Traversal stops at depth = 2.

**Time Complexity:** O(k₁ + k₂)  
**Space Complexity:** O(n + k₂)

Where:
- k₁ = number of first-degree connections
- k₂ = number of second-degree connections

---

### 3. Third-Degree Connections

Same BFS structure, extended to depth = 3.

**Time Complexity:** O(k₁ + k₂ + k₃)  
**Space Complexity:** O(n + k₃)

---

### 4. Interest-Based Friend Recommendation

Users are compared pairwise based on:

- Shared hobbies
- Shared music preferences
- Shared movie preferences

Each shared category adds 1 similarity point (0–3 scale).

Connections are suggested if similarity ≥ 1.

**Time Complexity:** O(n²)  
**Space Complexity:** O(n²)

---

## Scalability Considerations

The adjacency list structure scales efficiently for large graphs.

Potential optimizations:
- Limit recommendations to top-k most similar users
- Precompute similarity buckets
- Use priority queues for ranked suggestions
- Combine multi-degree traversal into a unified function

The current implementation is suitable for conceptual scalability to large user networks.

---

## Concepts Demonstrated

- Graph Representation
- Adjacency Lists
- Breadth-First Search (BFS)
- Queue Data Structure
- Sets for visited tracking
- Similarity Scoring
- Algorithmic Complexity Analysis
- System Design Thinking

---

## Repository Structure

```
social-network-graph-system/
│
├── notebooks/
│   └── social_network_graph_system.ipynb
│
├── report/
│   └── social_network_graph_system_report.pdf
```

---

## Educational Context

Developed as part of DTSC 5501: Data Structures & Algorithms.

This project demonstrates applied graph theory and traversal algorithms in a real-world social network context.
