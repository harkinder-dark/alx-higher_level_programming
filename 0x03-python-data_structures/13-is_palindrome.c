#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *left, *rigth, *current;
    if (*head == NULL)
    {
        return (1);
    }
    else
    {
        left = *head;
        current = left;
        rigth = current;
        while (rigth->next != NULL)
        {
            rigth = rigth->next;
        }
        if (left->n != rigth->n)
        {
            return (0);
        }
        else
        {
            while (left->next != rigth)
            {
                left = left->next;
                current = left;
                while (current->next != rigth)
                {
                    current = current->next;
                }
                rigth = current;
                if (left->n != rigth->n)
                {
                    return (0);
                }
            }
            if (left->n == rigth->n)
            {
                return (1);
            }
            return (0);
        }
    }
}
