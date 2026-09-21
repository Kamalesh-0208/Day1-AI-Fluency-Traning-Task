from config import COURSE_FEES


def get_course_fee(course_code):
    course_code = course_code.upper().strip()

    if course_code in COURSE_FEES:
        return COURSE_FEES[course_code]

    return None


def compare_course_fees(course1, course2):
    fee1 = get_course_fee(course1)
    fee2 = get_course_fee(course2)

    if fee1 is None or fee2 is None:
        return None

    difference = fee1 - fee2

    return {
        "course1": course1.upper(),
        "course2": course2.upper(),
        "fee1": fee1,
        "fee2": fee2,
        "difference": difference
    }


def calculate_scholarship(course1, course2, scholarship_percent):
    fee1 = get_course_fee(course1)
    fee2 = get_course_fee(course2)

    if fee1 is None or fee2 is None:
        return None

    total = fee1 + fee2
    discount = total * scholarship_percent / 100
    final_total = total - discount

    return {
        "original_total": total,
        "discount": discount,
        "final_total": final_total
    }