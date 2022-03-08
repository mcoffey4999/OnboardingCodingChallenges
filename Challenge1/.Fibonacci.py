int ans = 0;
int start1 = 1;
int start2 = 2;
int initRes = 0;
for(int i = 0; i <= 4000; i++){
  if(start2 % 2 == 0){
    ans += start2;
  }
  initRes = start1 + start2;
  start1 = start2;
  start2 = initRes;
}
Console.WriteLine(ans);
