from social_network_graph_system.graph import SocialGraph
from social_network_graph_system.sample_data import GRAPH, HOBBIES, MOVIES, MUSIC


def main() -> None:
    network = SocialGraph(graph=GRAPH, hobbies=HOBBIES, music=MUSIC, movies=MOVIES)

    print("First degree:", network.first_degree_connections("user_id10"))
    print("Second degree:", sorted(network.second_degree_connections("user_id10")))
    print("Third degree:", sorted(network.third_degree_connections("user_id10")))
    print(
        "Interest-based recommendations for user_id10:",
        network.suggest_connections_based_on_interests()["user_id10"],
    )


if __name__ == "__main__":
    main()
