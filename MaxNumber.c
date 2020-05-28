#include <stdio.h>
void main(){
  int a,b,c;
  printf("Enter First Number \n");
  scanf("%d",&a);
  
  printf("Enter Second Number \n");
  scanf("%d",&b);
  
  printf("Enter Third Number \n");
  scanf("%d",&c);
  
  printf(" First Number = %d\n Second Number =%d\n Third Number =%d\n",a,b,c);
  
  /// Now Finding Largest Number ///
   
   
   // Condition Ke Aage ; Nahi Lagta ! 
   
   
   if (a>=b && a>=c)
   printf("The Largest Number is %d",a);
    
   else if (b>=a && b>=c)
   printf("The Largest Number is %d",b);
    
   else if (c>=a && c>=b)
   printf("The Largest Number is %d",c);



return 0;

}
    