{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6ace46c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter no of testcases=4\n",
      "Enter Emotional proximate value p =1\n",
      "Enter Emotional proximate decrement value x =1\n",
      "Enter Emotional proximate increment value y =1\n",
      "Enter index value z = 0 or 11\n",
      "1.01\n",
      "Enter Emotional proximate value p =1\n",
      "Enter Emotional proximate decrement value x =1\n",
      "Enter Emotional proximate increment value y =1\n",
      "Enter index value z = 0 or 10\n",
      "0.99\n",
      "Enter Emotional proximate value p =100\n",
      "Enter Emotional proximate decrement value x =3\n",
      "Enter Emotional proximate increment value y =5\n",
      "Enter index value z = 0 or 11\n",
      "105.0\n"
     ]
    }
   ],
   "source": [
    "T = int(input(\"Enter no of testcases=\"))\n",
    "for i in range(T):\n",
    "    p=int(input(\"Enter Emotional proximate value p =\"))\n",
    "    x=int(input(\"Enter Emotional proximate decrement value x =\"))\n",
    "    y=int(input(\"Enter Emotional proximate increment value y =\"))\n",
    "    z=int(input(\"Enter index value z = 0 or 1\"))\n",
    "    if z == 1: \n",
    "        print(((p*y)/100)+p)\n",
    "    else:\n",
    "        print(p-((p*x)/100))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "396295e9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c13b199e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
