import regx.regx as regx

def test_matchOne_valid():
    assert regx.matchOne('.', 'z')
    assert regx.matchOne('a', 'a')
    assert regx.matchOne('', 'a')

def test_matchOne_invalid():
    assert not regx.matchOne('a', 'b')
    assert not regx.matchOne('p', '')
