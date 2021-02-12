def _group(g, numStudents):
    """
    Iterates over pairs of students that will be having a converation together
    in the gth group.
    """
    if numStudents % 2 == 1:
        # l is the student to the left of g (if they were in a circle)
        l = g + 1
        # r is the student to the right.
        r = g + numStudents - 1
        # We will never yield g.
        while l < r:
            yield tuple(sorted([l % numStudents, r % numStudents]))
            l += 1
            r -= 1
    else:
        # The number of students is even.
        # Choose the pairs as we would for the odd students and then pair up the
        # two remaining students.
        yield from _group(g, numStudents - 1)
        yield g, numStudents - 1


def matchStudents(numStudents: int):
    """
    Iterates over the groups of students that should be having a conversation.

    Each group is an iterator over indicies of students that should be having a
    conversation. 
    """
    if numStudents < 2:
        return

    # We know how many groups there will be, based on the parity of the number
    # of students.
    yield from map(
        lambda x: _group(x, numStudents),
        range(numStudents - (numStudents % 2 == 0))
    )


# Here is a potential use case:
if __name__ == "__main__":
    # The names of each student.
    students = [
        "Alice",
        "Bob",
        "Chris",
        "Danny",
    ]

    for i, group in enumerate(matchStudents(len(students)), 1):
        print(f"The next group of conversations (group {i}) will be between:")
        for a, b in group:
            print(f"\t{students[a]} and {students[b]}")
