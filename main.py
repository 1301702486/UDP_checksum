import matplotlib.pyplot as plt

src_port_num = 0b0110011001100000
dest_port_num = 0b0101010101010101
length = 0b1000111100001100
carry = 2 ** 16


def wrap_around_add(a, b):
    result = a + b
    while result > carry:
        result = result - carry + 1
    return result


def get_checksum_bin_str():
    result = wrap_around_add(wrap_around_add(src_port_num, dest_port_num), length)
    return flip_bits(format(result, '016b'))


def flip_bits(bin_str):
    result = ""
    for i in range(0, len(bin_str)):
        if bin_str[i] == '0':
            result += '1'
        else:
            result += '0'
    return result


def display():
    src_port_num_str = format(src_port_num, '016b')
    dest_port_num_str = format(dest_port_num, '016b')
    length_str = format(length, '016b')
    checksum_str = get_checksum_bin_str()
    checksum = int(checksum_str, 2)
    header_sum = wrap_around_add(wrap_around_add(wrap_around_add(src_port_num, dest_port_num), length), checksum)
    header_sum_str = format(header_sum, '016b')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.text(0.2, 0.6, 'src port num: ' + src_port_num_str)
    ax.text(0.2, 0.5, 'dest port num: ' + dest_port_num_str)
    ax.text(0.2, 0.4, 'length: ' + length_str)
    ax.text(0.2, 0.3, 'checksum: ' + checksum_str)
    ax.text(0.2, 0.2, 'header sum: ' + header_sum_str)
    table_val = [[src_port_num_str, dest_port_num_str], [length_str, checksum_str]]
    my_table = plt.table(table_val, cellLoc='center', colWidths=[0.4] * 2, loc='top')
    ax.text(0.5, 0.95, 'UDP segment header', verticalalignment='center', horizontalalignment='center')
    plt.axis('off')
    plt.show()


display()
