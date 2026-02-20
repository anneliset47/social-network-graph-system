from social_network_graph_system.graph import SocialGraph
from social_network_graph_system.sample_data import GRAPH, HOBBIES, MOVIES, MUSIC


def build_graph() -> SocialGraph:
    return SocialGraph(graph=GRAPH, hobbies=HOBBIES, music=MUSIC, movies=MOVIES)


def test_first_degree_connections() -> None:
    graph = build_graph()
    assert graph.first_degree_connections("user_id10") == ["user_id9"]


def test_second_degree_connections() -> None:
    graph = build_graph()
    assert graph.second_degree_connections("user_id10") == {
        "user_id2",
        "user_id3",
        "user_id4",
        "user_id5",
        "user_id6",
        "user_id7",
        "user_id8",
    }


def test_third_degree_connections() -> None:
    graph = build_graph()
    assert graph.third_degree_connections("user_id10") == {"user_id1"}


def test_recommendation_excludes_existing_friendships() -> None:
    graph = build_graph()
    recommendations = graph.suggest_connections_based_on_interests()
    assert "user_id9" not in recommendations["user_id10"]


def test_recommendation_scores() -> None:
    graph = build_graph()
    recommendations = graph.suggest_connections_based_on_interests()
    assert recommendations["user_id10"]["user_id2"] == 1
    assert recommendations["user_id10"]["user_id7"] == 1
