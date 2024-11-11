def gen_perms(perm_str, rem_dup=True):
    if len(perm_str)==0:
        return [""]
    results = gen_perms(perm_str[1:], rem_dup)
    results2 = []
    for result in results:
        for i in range(len(result) + 1):
            results2.append(result[:i] + perm_str[0] + result[i:])
    if (rem_dup):
        results2=list(set(results2))
    return results2


if __name__=="__main__":
    print(gen_perms("aaaaa", False))



