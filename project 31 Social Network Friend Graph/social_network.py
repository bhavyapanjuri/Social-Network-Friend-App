"""
Social Network Friend Graph System
Simple implementation using graph data structure
"""

from collections import deque


class SocialNetwork:
    
    def __init__(self):
        # Store friendships as adjacency list: {user: {friends}}
        self.graph = {}
    
    def add_user(self, user):
        # Add new user to network
        if user not in self.graph:
            self.graph[user] = set()
            print(f"[+] User '{user}' added")
        else:
            print(f"[!] User '{user}' already exists")
    
    def add_friendship(self, user1, user2):
        # Create bidirectional friendship between two users
        if user1 not in self.graph or user2 not in self.graph:
            print("[!] One or both users do not exist")
            return
        
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)
        print(f"[+] Friendship created: '{user1}' <-> '{user2}'")
    
    def get_friends(self, user):
        # Get all friends of a user
        if user not in self.graph:
            print(f"[!] User '{user}' not found")
            return []
        
        friends = list(self.graph[user])
        print(f"Friends of '{user}': {', '.join(friends) if friends else 'None'}")
        return friends
    
    def mutual_friends(self, user1, user2):
        # Find common friends using set intersection
        if user1 not in self.graph or user2 not in self.graph:
            print("[!] One or both users do not exist")
            return []
        
        mutual = list(self.graph[user1] & self.graph[user2])
        print(f"Mutual friends: {', '.join(mutual) if mutual else 'None'}")
        return mutual
    
    def shortest_path(self, user1, user2):
        # Find shortest connection path using BFS algorithm
        if user1 not in self.graph or user2 not in self.graph:
            print("[!] One or both users do not exist")
            return []
        
        # BFS: queue stores (current_user, path_to_current)
        queue = deque([(user1, [user1])])
        visited = {user1}
        
        while queue:
            current, path = queue.popleft()
            
            # Check each friend of current user
            for friend in self.graph[current]:
                if friend == user2:
                    final_path = path + [friend]
                    print(f"Shortest path: {' -> '.join(final_path)}")
                    return final_path
                
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, path + [friend]))
        
        print("[!] No connection found")
        return []
    
    def recommend_friends(self, user):
        # Suggest friends based on friends-of-friends
        if user not in self.graph:
            print(f"[!] User '{user}' not found")
            return []
        
        recommendations = {}
        
        # Check friends of each friend
        for friend in self.graph[user]:
            for friend_of_friend in self.graph[friend]:
                # Skip if it's the user or already a friend
                if friend_of_friend != user and friend_of_friend not in self.graph[user]:
                    recommendations[friend_of_friend] = recommendations.get(friend_of_friend, 0) + 1
        
        # Sort by number of mutual connections
        sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        
        if sorted_recs:
            print(f"\nRecommendations for '{user}':")
            for person, count in sorted_recs:
                print(f"  - {person} ({count} mutual)")
        else:
            print(f"No recommendations for '{user}'")
        
        return [person for person, _ in sorted_recs]
    
    def display_network(self):
        # Display entire network graph
        print("\n" + "="*40)
        print("SOCIAL NETWORK GRAPH")
        print("="*40)
        for user, friends in self.graph.items():
            print(f"{user}: {', '.join(friends) if friends else '(no friends)'}")
        print("="*40 + "\n")


# Demo
if __name__ == "__main__":
    
    print("\n*** SOCIAL NETWORK DEMO ***\n")
    
    # Create network
    network = SocialNetwork()
    
    # Add users
    print("--- Adding Users ---")
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_user("Charlie")
    network.add_user("David")
    network.add_user("Eve")
    
    # Create friendships
    print("\n--- Creating Friendships ---")
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Bob", "Charlie")
    network.add_friendship("Bob", "David")
    network.add_friendship("Charlie", "Eve")
    
    # Display network
    network.display_network()
    
    # Get friends
    print("--- Friend Lists ---")
    network.get_friends("Alice")
    network.get_friends("Bob")
    
    # Find mutual friends
    print("\n--- Mutual Friends ---")
    network.mutual_friends("Alice", "Bob")
    
    # Find shortest path
    print("\n--- Shortest Path ---")
    network.shortest_path("Alice", "David")
    network.shortest_path("Alice", "Eve")
    
    # Friend recommendations
    print("\n--- Recommendations ---")
    network.recommend_friends("Alice")
    
    print("\n[+] Demo completed!\n")
