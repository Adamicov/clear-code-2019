GB_MB_FACTOR = 1024


def calculate(usb_size, memes):

    max_weight = usb_size * GB_MB_FACTOR
    rows_number = len(memes)
    calculation_table = [[0 for i in range(max_weight + 1)]
                         for i in range(rows_number + 1)]

    for i in range(rows_number+1):
        for j in range(max_weight+1):

            meme_weight = memes[i-1][1]
            meme_value = memes[i-1][2]
            row_up = i - 1

            if i == 0 or j == 0:
                calculation_table[i][j] = 0
            elif meme_weight <= j:
                dp_col = j - meme_weight
                calculation_table[i][j] = max(
                    meme_value + calculation_table[row_up][dp_col],
                    calculation_table[row_up][j]
                )
            else:
                calculation_table[i][j] = calculation_table[row_up][j]

    max_memes_value = calculation_table[rows_number][max_weight]

    if max_memes_value == 0:
        return (max_memes_value, set())

    best_memes_set = retrieve_best_memes(
        max_weight, rows_number, calculation_table, max_memes_value, memes)

    return (max_memes_value, best_memes_set)


def retrieve_best_memes(max_weight, rows_number, calculation_table, max_memes_value, memes):

    current_value = max_memes_value
    current_weight = max_weight
    best_memes_set = set()

    for i in range(rows_number, 0, -1):

        row_up = i - 1

        if current_value != calculation_table[row_up][current_weight]:
            name, weight, value = memes[row_up]
            best_memes_set.add(name)
            current_value -= value
            current_weight -= weight

    return best_memes_set