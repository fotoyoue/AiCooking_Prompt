def A(m, n):
  """
  Ackermann's function using memoization technique (dynamic programming).

  Args:
      m: An integer.
      n: An integer.

  Returns:
      The value of Ackermann's function A(m, n).
  """

  # Create a memoization dictionary to store previously computed results
  memo = {}

  def helper(m, n):
    """
    Helper function for memoization.

    Args:
        m: An integer.
        n: An integer.

    Returns:
        The value of Ackermann's function A(m, n).
    """
    if (m, n) in memo:
      return memo[(m, n)]
    if m == 0:
      result = n + 1
    elif m > 0 and n == 0:
      result = helper(m - 1, 1)
    else:
      result = helper(m - 1, helper(m, n - 1))
    memo[(m, n)] = result
    return result

  return helper(m, n)

# Example usage
print(A(3, 8))

