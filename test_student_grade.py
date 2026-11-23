from student_grade import average, grade, is_pass
def test_average():
    assert average([90, 80, 70]) == 80
def test_grade_s():
    assert grade(95) == "S"
def test_grade_a():
    assert grade(85) == "A"
def test_grade_b():
    assert grade(70) == "B"
def test_grade_f():
    assert grade(39) == "F"
def test_pass_all_subjects():
    assert is_pass([40, 50, 60]) is True
def test_fail_if_one_subject_below_40():
    assert is_pass([90, 35, 80]) is False