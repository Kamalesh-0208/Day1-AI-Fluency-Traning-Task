# Day 2 – Reasoning and Agentic AI Analysis

## 1. Introduction

This task compares different approaches used by AI systems to solve reasoning problems:

1. Direct Prompting
2. Chain-of-Thought (CoT)
3. ReAct (Reasoning + Acting)
4. Self-Consistency

The comparison focuses on reasoning depth, tool usage, transparency, reliability, cost/speed, and consistency.

---

## 2. Scenario

The scenario used in this task is a college course-fee assistant.

The AI agent is given course fees, scholarship percentages, and questions involving calculations. The agent can use external tools to obtain course-fee information and perform the required reasoning.

The main question used for the ReAct experiment was:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship?

---

## 3. Direct Prompting

Direct prompting asks the model to answer the question directly without explicitly requesting a step-by-step reasoning process.

### Observation

The model can provide the correct answer quickly for simple reasoning questions.

### Advantages

- Simple to implement
- Fast response
- Low complexity
- Suitable for straightforward questions

### Limitations

- Reasoning process is less transparent
- More difficult to verify intermediate calculations
- May be less reliable for complex multi-step problems

---

## 4. Chain-of-Thought (CoT)

Chain-of-Thought prompting asks the model to solve the problem using explicit intermediate steps.

### Observation

For the course-fee calculation, the model showed the calculation step by step:

1. Calculate the total course fee.
2. Calculate the scholarship amount.
3. Calculate the payable amount.
4. Divide the amount into instalments when required.
5. Provide the final answer.

For example, the instalment calculation produced:

**₹9,562.50 per instalment**

### Advantages

- Makes intermediate reasoning easier to understand
- Helps verify calculations
- Useful for multi-step reasoning problems

### Limitations

- Produces longer responses
- Can take more time/tokens than direct prompting
- Explicit reasoning does not automatically guarantee correctness

---

## 5. ReAct (Reasoning + Acting)

ReAct combines reasoning with actions such as calling external tools.

### Observation

For the comparison question, the agent selected the course-fee tool multiple times to obtain the required course fees before producing the final answer.

The final result was:

- CS101 + AI202 with 10% scholarship = ₹27,000
- All three courses with 25% scholarship = ₹33,750
- Difference = ₹6,750

Therefore, the first option has the lower calculated cost.

### Advantages

- Can interact with external tools
- Suitable for questions requiring external information
- Makes tool usage observable through the action trace
- Can solve multi-step tasks involving information retrieval and reasoning

### Limitations

- More complex to implement
- Requires tool definitions and execution
- Multiple tool calls can increase latency and cost
- Errors can occur during tool selection or tool execution

---

## 6. Self-Consistency

Self-Consistency solves the same question multiple times and uses the majority answer.

In this experiment, the question was run five times.

### Observed Outputs

The five runs produced equivalent answers with minor formatting differences:

- 9,562.5
- 9,562.50
- Rs. 9,562.50
- 9,562.50 rupees
- Rs. 9,562.50 per instalment

The numerical answer was consistent across the runs.

### Observation

The experiment also showed that exact-string majority voting can treat differently formatted versions of the same numerical answer as different strings. Therefore, answer normalization would improve the voting mechanism.

### Advantages

- Can improve reliability when model outputs vary
- Useful for reasoning problems where multiple independent solutions can be generated
- Provides a way to identify a commonly occurring answer

### Limitations

- Requires multiple model calls
- Increases cost and execution time
- Exact string matching may fail when answers are numerically identical but formatted differently

---

## 7. Comparison

| Approach | Reasoning Depth | Tool Use | Transparency | Speed | Consistency |
|---|---|---|---|---|---|
| Direct Prompting | Low | No | Low | High | Depends on prompt |
| Chain-of-Thought | High | No | Higher | Medium | Depends on model |
| ReAct | High | Yes | High | Lower | Depends on tools and model |
| Self-Consistency | Multiple reasoning attempts | Optional | Medium | Lower | Higher through repeated answers |

---

## 8. Suitability Analysis

### Direct Prompting

Suitable for simple questions where the required information is already available and only a short answer is needed.

### Chain-of-Thought

Suitable for multi-step mathematical and logical reasoning where intermediate calculations are useful for verification.

### ReAct

Suitable when the AI needs to interact with external tools or retrieve information before completing the task.

### Self-Consistency

Suitable when reliability is important and additional model calls are acceptable.

---

## 9. Overall Conclusion

The experiments show that different prompting and agentic approaches are useful for different types of problems.

Direct prompting is simple and fast. Chain-of-Thought is useful for structured multi-step reasoning. ReAct is useful when external tools or information are required. Self-Consistency can improve reliability by comparing multiple generated answers, although it increases computational cost.

Therefore, the appropriate approach depends on the problem requirements, especially the need for reasoning, tool usage, transparency, speed, and reliability.