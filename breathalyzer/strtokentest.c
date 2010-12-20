#include <stdio.h>
#include <string.h>

struct str_list
{
    char *str;
    struct str_list *next;
};

int main()
{
    char test[] = "The quick brown fox.";
    char delim[] = " ";
    struct str_list *head;
    head->next = NULL;
    head->str = strtok(test, delim);
    struct str_list *iter = head;
    while (iter->str != NULL)
    {
        iter = iter->next;
        iter->str = strtok(NULL, delim);
        iter->next = NULL;
    }
    iter = head;
    while (iter)
    {
        printf("\"%s\"\n", iter->str);
        iter = iter->next;
    }
}
