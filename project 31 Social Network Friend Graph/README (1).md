# 🌐 Social Network Friend Graph System

A Python-based social networking system that models friendships using graph data structures, enabling users to connect, find mutual friends, discover connection paths, and receive friend recommendations.

---

## 📋 Project Overview

This system simulates how social media platforms like Facebook or LinkedIn manage user relationships. It represents:
- **Users** as nodes (vertices)
- **Friendships** as edges (connections)

The graph structure enables efficient analysis of social connections and relationship patterns.

---

## ✨ Features

1. **Add Users** - Register new users to the network
2. **Create Friendships** - Connect two users as friends
3. **View Friends** - Display all friends of a user
4. **Mutual Friends** - Find common friends between two users
5. **Shortest Path** - Calculate the shortest connection between users (BFS algorithm)
6. **Friend Recommendations** - Suggest potential friends based on mutual connections

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Data Structures**: Graph (Adjacency List), Set, Dictionary, Queue
- **Algorithms**: Breadth-First Search (BFS), Set Intersection

---

## 📦 Requirements

### System Requirements
- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

### Python Modules Used
- `collections.deque` - For BFS queue implementation

---

## 🏗️ Architecture & Design

### System Architecture

```
┌─────────────────────────────────────────┐
│         User Interface (CLI)            │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      SocialNetwork Class (Core)         │
├─────────────────────────────────────────┤
│  • User Management                      │
│  • Friendship Management                │
│  • Graph Algorithms                     │
│  • Recommendation Engine                │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│    Graph Data Structure (Adjacency)     │
│         { user: {friends} }             │
└─────────────────────────────────────────┘
```

### Data Structure

**Adjacency List Representation:**
```python
{
  "Alice": {"Bob", "Charlie"},
  "Bob": {"Alice", "Charlie", "David"},
  "Charlie": {"Alice", "Bob", "Eve"}
}
```

### Core Components

1. **User Management Module**
   - Add new users
   - Validate user existence

2. **Friendship Manager**
   - Create bidirectional friendships
   - Prevent duplicate connections

3. **Graph Algorithms**
   - BFS for shortest path
   - Set operations for mutual friends

4. **Recommendation Engine**
   - Friends-of-friends analysis
   - Ranking by mutual connections

---

## 🔄 Working Flow

### Step-by-Step Process

```
1. User Registration
   ↓
2. Add Friendships (Undirected Edges)
   ↓
3. View Friend List
   ↓
4. Find Mutual Friends (Set Intersection)
   ↓
5. Calculate Shortest Path (BFS)
   ↓
6. Generate Recommendations (Friends-of-Friends)
```

### Example Workflow

```python
# Step 1: Create network
network = SocialNetwork()

# Step 2: Add users
network.add_user("Alice")
network.add_user("Bob")

# Step 3: Create friendship
network.add_friendship("Alice", "Bob")

# Step 4: View friends
network.get_friends("Alice")  # Output: Bob

# Step 5: Find mutual friends
network.mutual_friends("Alice", "Bob")

# Step 6: Find shortest path
network.shortest_path("Alice", "Charlie")

# Step 7: Get recommendations
network.recommend_friends("Alice")
```

---

## 🚀 Installation & Usage

### Installation

1. Clone or download the project:
```bash
cd "c:\Python-Projects\Social Network Friend Graph"
```

2. No additional installation needed (uses Python standard library)

### Running the Program

```bash
python social_network.py
```

### Expected Output

```
🌐 SOCIAL NETWORK FRIEND GRAPH SYSTEM

--- Adding Users ---
✓ User 'Alice' added successfully
✓ User 'Bob' added successfully
✓ User 'Charlie' added successfully
...

--- Creating Friendships ---
✓ Friendship created between 'Alice' and 'Bob'
✓ Friendship created between 'Alice' and 'Charlie'
...

==================================================
SOCIAL NETWORK GRAPH
==================================================
Alice: Bob, Charlie
Bob: Alice, Charlie, David
Charlie: Alice, Bob, Eve
...

--- Friend Lists ---
Friends of 'Alice': Bob, Charlie

--- Mutual Friends ---
Mutual friends of 'Alice' and 'Bob': Charlie

--- Shortest Connection Path ---
Shortest path: Alice → Bob → David

--- Friend Recommendations ---
Friend recommendations for 'Alice':
  • David (1 mutual connection(s))
  • Eve (1 mutual connection(s))

✓ Demo completed successfully!
```

---

## 🧠 Algorithms Explained

### 1. Breadth-First Search (BFS) - Shortest Path

**Purpose**: Find the shortest connection between two users

**How it works**:
1. Start from source user
2. Explore all direct friends (level 1)
3. Then explore friends of friends (level 2)
4. Continue until target user is found

**Time Complexity**: O(V + E) where V = users, E = friendships

### 2. Set Intersection - Mutual Friends

**Purpose**: Find common friends between two users

**How it works**:
```python
mutual = set(friends_of_user1) & set(friends_of_user2)
```

**Time Complexity**: O(min(n, m)) where n, m are friend counts

### 3. Friends-of-Friends - Recommendations

**Purpose**: Suggest new connections

**How it works**:
1. For each friend of the user
2. Check their friends (friends-of-friends)
3. Exclude existing friends and self
4. Rank by number of mutual connections

**Time Complexity**: O(F × F) where F = average friends per user

---

## 📊 Example Network Graph

```
    Alice ─── Bob ─── David ─── Frank
      │        │
   Charlie ─── │
      │
     Eve
```

**Relationships**:
- Alice ↔ Bob, Charlie
- Bob ↔ Alice, Charlie, David
- Charlie ↔ Alice, Bob, Eve
- David ↔ Bob, Frank
- Frank ↔ David

---

## 🎯 Key Concepts Demonstrated

- **Graph Theory**: Undirected graph representation
- **Data Structures**: Adjacency list, sets, queues
- **Algorithms**: BFS traversal, set operations
- **Object-Oriented Programming**: Class-based design
- **Social Network Analysis**: Connection patterns, recommendations

---

## 🔧 Customization

### Adding Interactive Menu

You can extend the main function to include a menu-driven interface:

```python
def interactive_menu():
    network = SocialNetwork()
    while True:
        print("\n1. Add User")
        print("2. Add Friendship")
        print("3. View Friends")
        print("4. Find Mutual Friends")
        print("5. Shortest Path")
        print("6. Recommendations")
        print("7. Exit")
        choice = input("Enter choice: ")
        # Handle choices...
```

---

## 📈 Future Enhancements

- ✅ Add remove friendship functionality
- ✅ Implement user profiles with additional data
- ✅ Add graph visualization using matplotlib/networkx
- ✅ Persistent storage using JSON/SQLite
- ✅ Web interface using Flask/Django
- ✅ Community detection algorithms
- ✅ Influence score calculation

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

Created as a demonstration of graph algorithms and social network modeling in Python.

---

## 🤝 Contributing

Feel free to fork, modify, and enhance this project for learning purposes.

---

**Happy Coding! 🚀**
