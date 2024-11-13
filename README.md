# Invariant-Driven-Algorithms

## Overview

**Invariant-Driven-Algorithms** is a collection of algorithm problems solved using **invariant-based reasoning**. This approach isn't just about finding solutions but understanding the deeper properties (**invariants**) that help shape them. This repository features:

- Python code for quick prototyping and testing.
- The use of **LLMs** (Language Models) to generate insights and alternative approaches.
- Formal verification with **Lean**, supported by tools like **LeanDojo** for proof checking.

## Why Invariants?

Invariants are properties that stay true throughout the execution of an algorithm. By focusing on invariants, we can:

- Simplify the design and reasoning of solutions.
- Ensure the algorithms are robust and free from errors.
- Gain better insights into edge cases and correctness.

## How Solutions Are Structured

Each problem typically comes with two versions of the solution:

1. **Optimized Solution**: This is the main function, designed to be efficient in terms of time and space complexity.
2. **Reference Solution (`ref`)**: A simpler, often brute-force implementation that serves as a baseline for testing.

The `ref` function is used for **equivalence checking**, where we ensure that the optimized solution produces the same results as the reference solution. This helps confirm the correctness of the optimized approach without needing a formal proof.

### What About Invariant-Based Correctness?

In some cases, correctness is built directly into the invariants, and the `ref` function isn’t needed. For these problems, we use **Lean** and dependent types to formally verify that the solution meets the specified properties.

In the code, you’ll find `assert` statements used to express invariants. These statements often appear before loops, at the end of loop bodies, and after loops. An invariant typically refers to the condition that holds true throughout the loop's execution.

## Problem Index

| #  | Problem Name                          | Problem Statement                                                                 | Category     | Python Solution                                     |
|----|---------------------------------------|------------------------------------------------------------------------------------|--------------|-----------------------------------------------------|
| 1  | Count Distinct Absolute Values        | Given a sorted list of integers, count the number of distinct absolute values.     | Two Pointers | [Solution](./problems/1.%20countDistinctAbsoluteValues.py) |
| 2  | kSum        | Given an integer `target`, a number `k>=2`, and a list of integers, find all k-tuples that sum up to `target`.     | Two Pointers | [Solution](./problems/2.%20kSum.py) |
| 3  | minInRotated        | Find the minimum in a rotated and sorted array.     | Binary Search | [Solution](./problems/3.%20minInRotated.py) |