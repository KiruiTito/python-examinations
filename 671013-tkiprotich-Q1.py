QUESTION 1
def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):
    """
    This function calculates the net salary after tax based on hourly rate,
    hours worked, and tax rate.
    
    Parameters:
    hourly_rate (float): The hourly wage of the employee.
    hours_worked (float): The number of hours worked by the employee.
    tax_rate (float): The rate at which tax is deducted from the salary. Default is 15%.
    
    Returns:
    float: The net salary after tax.
    """
    # Calculating the gross salary
    gross_salary = hourly_rate * hours_worked
    
    # Deducting tax from the gross salary
    tax = gross_salary * tax_rate
    
    # Calculating the net salary
    net_salary = gross_salary - tax
    
    return net_salary



