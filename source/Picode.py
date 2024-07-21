class Solution():
    # 获取next数组
    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T) - 1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]

            else:
                j = next_val[j]
        return next_val

    def kmp(self, S, T):
        i = 0
        j = 0
        next = self.get_next(T)
        while i < len(S) and j < len(T):
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(T):
            return i - j
        else:
            return -1


def return_bir(birthday):
    filename = '0.1Billion.txt'
    with open(filename) as file_object:
        contents = file_object.read()
    # print(contents)
    if birthday in contents:
        a = Solution()
        return (a.kmp(contents, birthday))
    else:
        return (-1)


if __name__ == "__main__":
    birthday = '991127'
    # birthday = input("Enter your birthday,in the form yyyymmdd: ")
    outcome = return_bir(birthday)
    if outcome != -1:
        print("your birthday appears in the first billion digits of pi!")
        print(outcome)
    else:
        print('your birthday does not appear in the first billion of pi!')
