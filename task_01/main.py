def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()

                if not line:
                    continue

                try:
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError as e:
                    raise ValueError(
                        f"Invalid salary file format in line: '{line}'"
                    ) from e

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Salary file not found: '{path}'"
        ) from e

    if count == 0:
        return 0, 0.0

    average = total / count

    return total, average
