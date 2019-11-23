# christmas tree


def starting_tree_width(num_of_trees):
    tree_proportion = -1
    half_tree_width = 0
    tree_section = 3
    if num_of_trees == 1:
        return 0, 4
    for tree_width in range(0, num_of_trees):
        tree_section += 1
        if tree_width % 4 == 0 and tree_width != 0:
            tree_proportion += 1
        half_tree_width = 3 * tree_width + tree_proportion
    return half_tree_width, tree_section


def get_max_tree_width(num_of_trees):
    final_tree_width,tree_section = starting_tree_width(num_of_trees)
    return 2*(final_tree_width+tree_section)-1


def draw_trunk(num_of_trees, max_width):
    i = 1
    while i <= num_of_trees:
        print((num_of_trees*'|').center(max_width,' '))
        i += 1


def draw_trees(num_of_trees):
    max_tree_width = get_max_tree_width(num_of_trees)

    if num_of_trees < 1:
        print("")
    for tree in range(1,num_of_trees+1):
        start, section = starting_tree_width(tree)
        for i in range(start,start+section):
            leaves = ((2 * i ) + 1) * '*'
            print(leaves.center(max_tree_width,' '))
    draw_trunk(num_of_trees, max_tree_width)


# Driver Code
draw_trees(5)
