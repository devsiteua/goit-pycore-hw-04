def get_cats_info(path: str) -> list[dict[str, str]]:
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()

                if not line:
                    continue

                try:
                    cat_id, cat_name, cat_age = line.split(',')
                    cats.append({'id': cat_id, 'name': cat_name, 'age': cat_age})

                except ValueError as e:
                    raise ValueError(
                        f"Invalid cats file format in line: '{line}'"
                    ) from e

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Cats file not found: '{path}'"
        ) from e

    return cats
