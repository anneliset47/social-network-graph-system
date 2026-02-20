from __future__ import annotations

from collections import deque


class SocialGraph:
    def __init__(
        self,
        graph: dict[str, dict[str, int]],
        hobbies: dict[str, str],
        music: dict[str, str],
        movies: dict[str, str],
    ) -> None:
        self.graph = graph
        self.hobbies = hobbies
        self.music = music
        self.movies = movies

    def first_degree_connections(self, user_id: str) -> list[str]:
        return sorted(self.graph.get(user_id, {}).keys())

    def second_degree_connections(self, user_id: str) -> set[str]:
        return self.connections_at_degree(user_id=user_id, degree=2)

    def third_degree_connections(self, user_id: str) -> set[str]:
        return self.connections_at_degree(user_id=user_id, degree=3)

    def connections_at_degree(self, user_id: str, degree: int) -> set[str]:
        if user_id not in self.graph or degree < 1:
            return set()

        distances = self._shortest_path_distances(user_id)
        return {candidate for candidate, distance in distances.items() if distance == degree}

    def suggest_connections_based_on_interests(self) -> dict[str, dict[str, int]]:
        suggested_graph: dict[str, dict[str, int]] = {}

        for user in self.graph:
            suggested_graph[user] = {}
            for candidate in self.graph:
                if user == candidate or candidate in self.graph[user]:
                    continue

                score = self._similarity_score(user, candidate)
                if score > 0:
                    suggested_graph[user][candidate] = score

        return suggested_graph

    def _shortest_path_distances(self, source_user: str) -> dict[str, int]:
        distances: dict[str, int] = {source_user: 0}
        queue: deque[str] = deque([source_user])

        while queue:
            current = queue.popleft()
            current_distance = distances[current]

            for neighbor in self.graph.get(current, {}):
                if neighbor in distances:
                    continue
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

        return distances

    def _similarity_score(self, user_id: str, candidate_id: str) -> int:
        score = 0
        if self.hobbies.get(user_id) == self.hobbies.get(candidate_id):
            score += 1
        if self.music.get(user_id) == self.music.get(candidate_id):
            score += 1
        if self.movies.get(user_id) == self.movies.get(candidate_id):
            score += 1
        return score
