const tour=[['Start with an eligible seller',
    'The example seller is under the €100,000 annual gross-revenue ceiling. Eligibility is a rule, not a judgement about the offer.',
    'seller'],
  ['Back the promise with settled value',
    'Only €1,240 is available. The €215 pending compute estimate is visible, but contributes €0 to the spendable balance.',
    'funding'],
  ['Agree on the minimum test',
    'The seller sees the 12,000-impression minimum, €840 allocation, and maximum commission before activation.',
    'campaign'],
  ['Record delivery without a reach cap',
    'The initial allocation guarantees a meaningful minimum. Proven, fundable campaigns may earn another tranche.',
    'campaign'],
  ['Review each sale',
    'A duplicate or refund does not become commission. One order is held through its return window.',
    'sales'],
  ['Keep compute voluntary',
    'The contributor controls participation and resource boundaries. These switches only change this fictional demo.',
    'compute']];
let tourIndex=0;
const nav=[...document.querySelectorAll('.nav button')];
function go(id){
  document.querySelectorAll('.screen').forEach(x=>x.classList.toggle('active',
  x.id===id));
  nav.forEach(x=>x.classList.toggle('active',
  x.dataset.screen===id));
  window.scrollTo({
    top:0,
    behavior:'smooth'}
  )}
nav.forEach(b=>b.addEventListener('click',
()=>go(b.dataset.screen)));
function showTour(){
  let t=tour[tourIndex];
  document.getElementById('tourNum').textContent=tourIndex+1;
  document.getElementById('tourTitle').textContent=t[0];
  document.getElementById('tourText').textContent=t[1];
  document.getElementById('nextTour').textContent=tourIndex===tour.length-1?'Restart tour ↺':'Next step →';
  go(t[2])}
document.getElementById('nextTour').onclick=()=>{
  tourIndex=(tourIndex+1)%tour.length;
  showTour()}
;
document.querySelector('.hero .btn').onclick=()=>{
  tourIndex=0;
  showTour()}
;
let fund=1240;
document.getElementById('addFunds').onclick=()=>{
  fund+=100;
  ['metricFund',
    'fundBig',
    'fundAvailable'].forEach(id=>document.getElementById(id).textContent='€'+fund.toLocaleString('en'));
  document.getElementById('fundReserve').textContent='€'+(fund-840).toLocaleString('en');
  document.getElementById('fundAction').textContent='Demo contribution added. Campaign funding unchanged.';
  toast('Fictional contribution added to this browser demo.')}
;
document.getElementById('acceptTerms').onclick=()=>{
  document.getElementById('acceptTerms').textContent='Terms accepted · demo';
  document.getElementById('acceptTerms').classList.remove('secondary');
  toast('Sample terms accepted locally; no campaign was launched.')}
;
document.getElementById('reviewSale').onclick=()=>{
  toast('Next sample sale reviewed: pending the return window.');
  document.getElementById('reviewSale').textContent='Queue reviewed'}
;
document.getElementById('computeToggle').onchange=e=>{
  const state=document.getElementById('computeState');
  state.textContent=e.target.checked?'Opted in · demo':'Paused · demo';
  state.className=e.target.checked?'status done':'status wait';
  toast(e.target.checked?'Demo consent enabled.':'Demo participation paused.')}
;
function toast(s){
  let t=document.getElementById('toast');
  t.textContent=s;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),
  2600)}
