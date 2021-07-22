import regx.regx as regx


def test_matchOne_valid():
    assert regx.matchOne(".", "z")
    assert regx.matchOne("a", "a")
    assert regx.matchOne("", "a")


def test_matchOne_invalid():
    assert not regx.matchOne("a", "b")
    assert not regx.matchOne("p", "")


def test_search():
    assert regx.search("bc", "abcd")
    assert not regx.search("bc", "ac")
    assert regx.search("bc", "abcd")


def test_search_with_end_of_string():
    assert regx.search("a$", "aa")
    assert not regx.search("a$", "abaaaab")


def test_search_with_start_of_string():
    assert regx.search("^a", "ab")
    assert not regx.search("^a", "baaaab")


def test_search_with_question_mark():
    assert regx.search("ab?c", "ac")
    assert regx.search("ab?c", "abc")
    assert regx.search("a?b?c?", "")
    assert regx.search("ab?c", "abc")
