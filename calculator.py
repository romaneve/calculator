"""
Calculator library contining basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    return first_term / second_term


def average(in_list):
    return sum(in_list) / len(in_list)


def handicap(base, pct, ave):
    return (base - ave)*pct
