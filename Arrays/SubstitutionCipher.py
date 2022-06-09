"""
file: SubstitutionCipher.py
description: This program prints freqeuncy count of each letter in sorted way for the provided sentence
language: python3
author: Aryan Singh, as2886
author: Rishi Sharma, rs5501
"""

import re


def main():
    input_string = "Ozgvi, rg dzh hzrw gsv nzm xznv uiln gsv mligs, uiln Ilkvih Tzgv. Sv xznv lm ullg, ovzwrmt srh ozwvm slihv yb gsv yirwov. Rg dzh ozgv zugvimllm zmw gsv ilkvih, hzwwovih zmw gzmmvih hgzooh dviv zoivzwb xolhvw, gsv hgivvg vnkgb. Rg dzh slg yfg gsv nzm szw z yozxp xlzg gsildm levi srh hslfowvih. Sv wivd zggvmgrlm gl srnhvou. Sv hglkkvw rm uilmg lu gsv Low Mzizplig Rmm, hgllw gsviv uli z nlnvmg, orhgvmvw gl gsv sfyyfy lu elrxvh. Zh fhfzo, zg gsrh slfi, rg dzh ufoo lu kvlkov. Gsv hgizmtvi wrw mlg vmgvi gsv Low Mzizplig. Sv kfoovw srh slihv ufigsvi wldm gsv hgivvg gl zmlgsvi gzevim, z hnzoovi lmv, xzoovw Gsv Ulc. Mlg vmqlbrmt gsv yvhg lu ivkfgzgrlmh, rg dzh zonlhg vnkgb."
    cleaned_string = re.sub('[,?=.*]','',input_string)
    print(cleaned_string)
    count_dict = {}

    for index in cleaned_string.lower().strip():
        if index in count_dict:
            count_dict[index] += 1
        else:
            count_dict[index] = 1

    sorted_dict = {}
    sorted_val = sorted(count_dict, key=count_dict.get)
    for val in sorted_val:
        sorted_dict[val] = count_dict[val]
    sorted_dict.pop(" ")
    print(str(sorted_dict))
    # calculating the frequency
    total_sum = sum(sorted_dict.values())
    print("Alphabet", "Frequency")
    for value in sorted_dict:
        print(value, "\t\t", (sorted_dict[value] * 100)/total_sum)


if __name__ == '__main__':
    main()
