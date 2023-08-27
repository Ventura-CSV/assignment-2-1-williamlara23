def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = int(input("How many male students: "))
    females = int(input("How many female students: "))
    total = int(males)+ int(females)
    m_perc = float(males)/total
    f_perc = float(females)/total
    print("The total number of students: " + str(total))
    print("The total of males and females: " + str(males) +" "+str(females))
    print(f"The percentage of males and females:  {m_perc:,.2%} {f_perc:,.2%}")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
