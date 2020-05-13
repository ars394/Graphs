from util import Stack, Queue 
test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```

def earliest_ancestor(ancestors, starting_node):
    
    firsts = set()
    seconds = set()
    ancestor_dict = {}
    possible_answers = []
    
    for i in ancestors:
        firsts.add(i[0])
        seconds.add(i[1])
    
    ancestor_start_points = firsts - seconds
    #print('starts',ancestor_start_points)
    for i in ancestors:
        if i[0] not in ancestor_dict:
            ancestor_dict[i[0]] = [i[1]]
        else:
            ancestor_dict[i[0]].append(i[1])
    #print('dict',ancestor_dict)
    for i in ancestor_start_points:
        q = Queue()
        q.enqueue(i)
        path = [i]
        visited = set()

        while q.size() > 0:
            node = q.dequeue() 
            
            visited.add(node)
            if path[-1] == starting_node:
                break
            if node not in ancestor_dict:
                
                continue
            if starting_node == 7:
                print('this is the print',ancestor_dict[node])
            for i in ancestor_dict[node]:
                
                if i != starting_node and i not in visited:
                    
                    q.enqueue(i)
                    path.append(i)
                
                elif i == starting_node:
                    path.append(i)
                    possible_answers.append(path)
                    break

    print('poss', possible_answers)    
    answer = []
    for i in possible_answers:
        if len(i) > len(answer):
            answer = i
    if len(answer) > 0:
        return answer[0]   
    else:
        return -1