#include "lists.h"
/**
 * is_palindrome - palindrome
 *
 * @head: parameter
 * Return: int
 */
int is_palindrome(listint_t **head)
{
    listint_t *left, *rigth, *current;
    if (*head != NULL)
    {
        left = *head;
        
        if (left->next == NULL)
            return (1);

        rigth = left;    
        while (rigth->next != NULL)
            rigth = rigth->next;

        if (left->n != rigth->n)
            return (0);
        else
        {
            while (left->next != rigth)
            {
                left = left->next;
                current = left;
                
                while (current->next != rigth)
                    current = current->next;
                
                if (left->n != current->n)
                    return (0);

                rigth = current;
            }

            if (left->n == rigth->n)
                return (1);

            return (0);
        }
    }
    return (1);
}
