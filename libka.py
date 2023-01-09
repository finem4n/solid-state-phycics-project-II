def file_loader(plik):

    from numpy import delete
    from pandas import read_table

    df = read_table(plik,sep="\s+", skiprows=0, usecols=[0, 1], header=None)

    conv_arr = df.values

    x = delete(conv_arr, 1, axis=1)
    y = delete(conv_arr, 0, axis=1)

    x = x.ravel()
    y = y.ravel()

    return x, y