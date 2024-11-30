import day01

def test_greeting_is_hello():
    puzzle = day01.Day01Puzzle()
    assert puzzle.greeting() == "hello"