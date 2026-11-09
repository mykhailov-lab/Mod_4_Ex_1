def total_salary (salary_lines : list[str]) -> tuple[int, int] :
    if not salary_lines:
        return (0,0)
    total_salary = 0
    number_workers = 0
    for i in salary_lines:
        line_file = i.strip()
        if not line_file :
             continue
        name, salary_str = line_file. split(',')
        total_salary = float(salary_str) + total_salary
        number_workers = number_workers + 1
    if number_workers == 0:
        return (0,0)
    average_salary = total_salary / number_workers
    return (total_salary, average_salary)