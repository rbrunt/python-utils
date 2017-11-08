def traverse_dictionary(dictionary, selector, separator="."):
    if isinstance(selector, str):
        selector_list = selector.split(separator)
    elif isinstance(selector, list):
        selector_list = selector
    else:
        raise TypeError("Don't recognise selector type")

    max_depth = len(selector_list) - 1
    current_dict = dictionary
    for i in xrange(len(selector_list)):
        current_selector = selector_list[i]

        if i == max_depth:
            return current_dict[current_selector]
        else:
            current_dict = current_dict[current_selector]