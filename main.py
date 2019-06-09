
def calculate(usb_size, memes):
    max_weight = usb_size * 1024
    rows = len(memes)
    table = [[0 for i in range(max_weight + 1)]
             for i in range(rows + 1)]

    for i in range(rows+1):
        for j in range(max_weight+1):

            meme_weight = memes[i-1][1]
            meme_value = memes[i-1][2]
            row_up = i - 1

            if i == 0 or j == 0:
                table[i][j] = 0

            elif meme_weight <= j:
                dp_col = j - meme_weight
                table[i][j] = max(
                    meme_value + table[row_up][dp_col],
                    table[row_up][j]
                )

            else:
                table[i][j] = table[row_up][j]

    max_memes_value = table[rows][max_weight]
    best_memes_set = set()
    current_value = max_memes_value
    m = max_weight

    if max_memes_value == 0:
        return (max_memes_value, best_memes_set)

    for i in range(rows, 0, -1):

        row_up = i - 1

        if current_value != table[row_up][m]:
            name, weight, value = memes[row_up]
            best_memes_set.add(name)
            current_value -= value
            m -= weight

    return (max_memes_value, best_memes_set)


