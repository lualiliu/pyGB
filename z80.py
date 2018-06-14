class Z80():
	_r={
		'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'h':0, 'l':0, 'f':0,
		'sp':0, 'pc':0, 'i':0, 'r':0,
		'm':0,
		'ime':0
	};
	_rsv={
		'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'h':0, 'l':0, 'f':0
	};
	_clock={'m':0};
	_halt=0;
	_stop=0;

	def reset():
		Z80._r['a'] = 0; Z80._r['b']=0; Z80._r['c']=0; Z80._r['d']=0; Z80._r['e']=0; Z80._r['h']=0; Z80._r['l']=0; Z80._r['f']=0;
		Z80._r['sp']=0; Z80._r['pc']=0; Z80._r['i']=0; Z80._r['r']=0;
		Z80._r['m']=0;
		Z80._halt=0; Z80._stop=0;
		Z80._clock['m']=0;
		Z80._r['ime']=1;
		print("Z80 Reset.");
	def exec():
		Z80._r['r'] = (Z80._r['r']+1) & 127;
		Z80._map[MMU.rb(Z80._r['pc']+1)]();
		Z80._r['pc'] &= 65535;
		Z80._clock['m'] += Z80._r['m'];
	_map = [];
	_cbmap = [];
	def LDrr_bb(): Z80._r['b']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_bc(): Z80._r['b']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_bd(): Z80._r['b']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_be(): Z80._r['b']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_bh(): Z80._r['b']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_bl(): Z80._r['b']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_ba(): Z80._r['b']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_cb(): Z80._r['c']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_cc(): Z80._r['c']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_cd(): Z80._r['c']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_ce(): Z80._r['c']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_ch(): Z80._r['c']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_cl(): Z80._r['c']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_ca(): Z80._r['c']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_db(): Z80._r['d']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_dc(): Z80._r['d']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_dd(): Z80._r['d']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_de(): Z80._r['d']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_dh(): Z80._r['d']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_dl(): Z80._r['d']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_da(): Z80._r['d']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_eb(): Z80._r['e']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_ec(): Z80._r['e']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_ed(): Z80._r['e']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_ee(): Z80._r['e']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_eh(): Z80._r['e']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_el(): Z80._r['e']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_ea(): Z80._r['e']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_hb(): Z80._r['h']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_hc(): Z80._r['h']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_hd(): Z80._r['h']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_he(): Z80._r['h']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_hh(): Z80._r['h']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_hl(): Z80._r['h']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_ha(): Z80._r['h']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_lb(): Z80._r['l']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_lc(): Z80._r['l']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_ld(): Z80._r['l']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_le(): Z80._r['l']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_lh(): Z80._r['l']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_ll(): Z80._r['l']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_la(): Z80._r['l']=Z80._r['a']; Z80._r['m']=1;
	def LDrr_ab(): Z80._r['a']=Z80._r['b']; Z80._r['m']=1;
	def LDrr_ac(): Z80._r['a']=Z80._r['c']; Z80._r['m']=1;
	def LDrr_ad(): Z80._r['a']=Z80._r['d']; Z80._r['m']=1;
	def LDrr_ae(): Z80._r['a']=Z80._r['e']; Z80._r['m']=1;
	def LDrr_ah(): Z80._r['a']=Z80._r['h']; Z80._r['m']=1;
	def LDrr_al(): Z80._r['a']=Z80._r['l']; Z80._r['m']=1;
	def LDrr_aa(): Z80._r['a']=Z80._r['a']; Z80._r['m']=1;
	
print("CPU loaded");
