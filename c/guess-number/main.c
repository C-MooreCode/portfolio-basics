#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void){
  srand((unsigned)time(NULL));
  int secret = rand()%100+1, g=0, tries=0;
  printf("Guess 1..100:\n");
  while(scanf("%d",&g)==1){ tries++;
    if(g==secret){ printf("Correct in %d tries.\n", tries); break; }
    printf(g<secret ? "Higher\n" : "Lower\n");
  }
  return 0;
}
