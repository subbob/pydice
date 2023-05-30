from random import randint
from statistics import mean

def main():
    MyScores = GenStats(12)
    print (f"Average Score {mean(MyScores):.1f}")
    print(MyScores)

def RollDie(faces):
    return randint(1,faces)

def test_RollDie():
    # test to ensure result of RollDie(6) returns a value in range 1..6
    value = RollDie(6)
    assert value >= 1
    assert value <= 6

def RollDice(quantity, faces,min=0):
    if (min == 0):
        min = quantity

    while True:
        result=0;
        for i in range(quantity):
            result += RollDie(faces)
        if (result >= min):
            return result

def test_RollDice():
    # test to ensure RollDice(3,6) returns a value in range 3..18
    value = RollDice(3,6);
    assert value >= 3
    assert value <= 18

    # tests of average option, 10 & 16, ensuring the calls return results >= 10 & 16 respectively
    assert RollDice(3,6,10) >= 10
    assert RollDice(3,6,16) >= 16

def GenStats(average=0):
    
    while True:
        scores = [0,0,0,0,0,0]
        for i in range(len(scores)):
            scores[i] = RollDice(3,6)
        if (mean(scores) >= average):
            return scores

def test_GenStats():

    scores=GenStats()
    assert len(scores) == 6         # scores contains 6 items
    assert mean(scores) >= 3        # average of scors >= 3 and <= 18
    assert mean(scores) <= 18
    
    scores=GenStats(12)
    assert mean(scores) >= 12       # testing minimum average option

    # The test below checks that none of the values in scores is 0
    # However, I believe this test to be unnecessary due to the previous
    # tests of RollDie and RollDice
    test = (0 in scores)
    assert test is False

main()
