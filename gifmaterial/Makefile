OUTDIR:=../images
FORMAT:=mp4
IFLAGS:= -y
OFLAGS:= -an -pix_fmt yuv420p -c:v libx264

all: \
$(OUTDIR)/defmanip.$(FORMAT) \
$(OUTDIR)/crazyswarm.$(FORMAT) \
$(OUTDIR)/subopt.$(FORMAT) \
$(OUTDIR)/quadrl.$(FORMAT) \
$(OUTDIR)/gaps.$(FORMAT) \
$(OUTDIR)/linc.$(FORMAT) \

$(OUTDIR)/defmanip.$(FORMAT): defmanip_crop.mp4
	ffmpeg $(IFLAGS) -i $< -s 400x400 -r 30 -loop 0 $(OFLAGS) \
	$@

defmanip_crop.mp4: defmanip_trim.mp4
	ffmpeg $(IFLAGS) -i $< -filter:v "crop=1080:1080:260:0" $(OFLAGS) \
	$@

defmanip_trim.mp4: defmanip_circle_ours.mp4
	ffmpeg $(IFLAGS) -i $< -ss 00:01:34.30 -to 00:01:43.50 $(OFLAGS) \
	$@


# To make the GIMP curves .txt file, in the Curves tool choose menu > export
# with "use old format" enabled.
%_curves_ffmpeg.txt: %_curves_gimp.txt gimp2ffmpeg.py
	cat $< | python3 gimp2ffmpeg.py > $(OFLAGS) \
	$@

$(OUTDIR)/crazyswarm.$(FORMAT): crazyplan_tro_inside.mp4 crazyswarm_curves_ffmpeg.txt
	ffmpeg $(IFLAGS) -i $< \
	-ss 00:00:27.00 -to 00:00:37.00 \
	-filter:v "crop=1080:1080:400:0, curves=all='`cat crazyswarm_curves_ffmpeg.txt`'" \
	-s 400x400 \
	-loop 0 \
	$(OFLAGS) \
	$@

$(OUTDIR)/subopt.$(FORMAT): subopt_neighborhood_3d.mp4
	ffmpeg $(IFLAGS) -i $< \
	-filter:v "crop=980:980:50:50" \
	-s 400x400 \
	-loop 0 \
	$(OFLAGS) \
	$@


$(OUTDIR)/quadrl.$(FORMAT): medium_quad_throw.mp4 quadrl_curves_ffmpeg.txt
	ffmpeg $(IFLAGS) -i $< \
	-filter:v "crop=550:550:445:75, curves=all='`cat quadrl_curves_ffmpeg.txt`'" \
	-ss 03.40 -to 05.60 \
	-s 400x400 \
	-loop 0 \
	$(OFLAGS) \
	$@


$(OUTDIR)/gaps.$(FORMAT): gaps_pvtol_tuning.mp4
	ffmpeg $(IFLAGS) -i $< \
	-filter:v "crop=980:980:10:10" \
	-s 400x400 \
	-loop 0 \
	$(OFLAGS) \
	$@


$(OUTDIR)/linc.$(FORMAT): gvrbot_mars_yard.mov
	ffmpeg $(IFLAGS) -r:v "60/1" -i $< \
	-filter:v "crop=900:900:100+75*(t-3):0" \
	-ss 04.0 -to 15.0 \
	-s 400x400 \
	-loop 0 \
	-r:v "30/1" \
	$(OFLAGS) \
	$@
