// levenshtein.c
// http://en.wikipedia.org/wiki/Levenshtein_distance

#include <stdio.h>

int minimum(int a, int b, int c)
{
    if ((a <= b) && (a <= c))
        return a;
    else if ((b <= a) && (b <= c))
        return b;
    else
        return c;
}

int main()
{
    int m = 8;
    int n = 6;
    char s[] = "Saturday";
    char t[] = "Sunday";
    int d[m+1][n+1];
    
    int i, j;
    for(i = 0; i <= m; i++)
        d[i][0] = i;
    for(j = 0; j <= n; j++)
        d[0][j] = j;

    for(j = 1; j <= n; j++)
    {
        for(i = 1; i <= m; i++)
        {
            if (s[i] == t[j])
              d[i][j] = d[i-1][j-1];
            else
              d[i][j] = minimum(d[i-1][j] + 1,
                                d[i][j-1] + 1,
                                d[i-1][j-1] + 1);
        }
    }
    printf("Lev of Saturday and Sunday: %d\n", d[m][n]);
}
