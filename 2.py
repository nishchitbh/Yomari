# Add your imports here if required

# Important: Do not change function signature and mind your indenatation
def q2(x: int) -> int:
  # Write your code here below
  return str(bin(x))[2::].count('1') % 2
