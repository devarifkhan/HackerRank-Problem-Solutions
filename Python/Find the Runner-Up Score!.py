if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(list(set(sorted(arr)))[-2])