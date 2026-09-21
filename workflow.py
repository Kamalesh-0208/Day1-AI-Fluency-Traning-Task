from config import COURSE_FEES, QUESTIONS, banner


def workflow(question):
    question_lower = question.lower()

    # Question 1
    if "fee for ai202" in question_lower:
        return f"AI202 fee is ₹{COURSE_FEES['AI202']:,}."

    # Question 2
    elif "total fee" in question_lower and "10%" in question_lower:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        discounted_total = total * 0.90
        return f"Total after 10% scholarship is ₹{discounted_total:,.0f}."

    # Question 3
    elif "ds303" in question_lower and "cs101" in question_lower:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]

        if difference > 0:
            return f"Yes. DS303 is more expensive than CS101 by ₹{difference:,}."
        elif difference < 0:
            return f"No. DS303 is cheaper than CS101 by ₹{-difference:,}."
        else:
            return "DS303 and CS101 have the same fee."

    # Question 4
    elif "welcome message" in question_lower:
        return (
            "Welcome to the AI program!\n"
            "Wishing you an exciting journey of learning and innovation."
        )

    else:
        return "Sorry, this workflow does not have a rule for that question."


if __name__ == "__main__":
    banner("SYSTEM 2: RULE-BASED WORKFLOW")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)