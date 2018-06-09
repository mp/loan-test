# Whether a bank customer qualifies for a loan
# constants
MIN_SALARY = 20000.0
MIN_YEARS = 3

def main():
  # get the customers annual salary
  salary = float(input('Enter your annual salary: '))

  # Get number of years in the job
  years_on_job = int(input('Enter the number of years employed: '))

  # Check if customer qualifies for a loan

  if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
  else:
    print('You do not qualify for this loan.')

# Call the main function
main()