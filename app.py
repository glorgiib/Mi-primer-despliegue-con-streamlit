<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1T40YdV70LtqWwWloyBK1tI6t2ZYkAH3M#scrollTo=fCL7wnn1WE2K -->
<html lang="es" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="glorgiib.gegi@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./app.ipynb_files/recaptcha__es_419.js" crossorigin="anonymous" integrity="sha384-i02cZZeg3EeDob1Y8Bf8XH70Ib2c1tfUScRNJGOQjlKTy6j07e/2atE5ayb3MJH+" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./app.ipynb_files/recaptcha__es_419.js" crossorigin="anonymous" integrity="sha384-i02cZZeg3EeDob1Y8Bf8XH70Ib2c1tfUScRNJGOQjlKTy6j07e/2atE5ayb3MJH+" nonce=""></script><script type="text/javascript" async="" src="./app.ipynb_files/js" nonce=""></script><script src="./app.ipynb_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./app.ipynb_files/cb=gapi.loaded_0" nonce="" async=""></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Despliegue.ipynb - Colab</title><link href="./app.ipynb_files/css2" rel="stylesheet"><link href="./app.ipynb_files/css" rel="stylesheet"><script nonce="">
      window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    </script><script async="" src="./app.ipynb_files/analytics.js" nonce=""></script><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_yb{font:13px/27px Roboto,Arial,sans-serif;z-index:986}.gb_R{display:none}.gb_Q{background-size:32px 32px;border:0;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_kb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_kb.gb_Q{height:30px;width:30px}.gb_kb.gb_Q:hover,.gb_kb.gb_Q:active{box-shadow:none}.gb_lb{background:#fff;border:none;border-radius:50%;bottom:2px;box-shadow:0px 1px 2px 0px rgba(60,64,67,0.3),0px 1px 3px 1px rgba(60,64,67,0.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_mb{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25),(min-resolution:1.25dppx){.gb_Q::before,.gb_nb::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_4 .gb_nb::before{-webkit-transform:scale(scale(.416666667));transform:scale(scale(.416666667))}}.gb_Q:hover,.gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Q:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Q:active::after{background:rgba(0,0,0,.1);border-radius:50%;content:"";display:block;height:100%}.gb_ob{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_ob{width:auto}.gb_ob:hover,.gb_ob:focus{opacity:.85}.gb_pb .gb_ob,.gb_pb .gb_qb{line-height:26px}#gb#gb.gb_pb a.gb_ob,.gb_pb .gb_qb{font-size:11px;height:auto}.gb_rb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_0a:hover .gb_rb{opacity:.85}.gb_Xa>.gb_z{padding:3px 3px 3px 4px}.gb_sb.gb_jb{color:#fff}.gb_2 .gb_ob,.gb_2 .gb_rb{opacity:1}#gb#gb.gb_2.gb_2 a.gb_ob,#gb#gb .gb_2.gb_2 a.gb_ob{color:#fff}.gb_2.gb_2 .gb_rb{border-top-color:#fff;opacity:1}.gb_la .gb_Q:hover,.gb_2 .gb_Q:hover,.gb_la .gb_Q:focus,.gb_2 .gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.2)}.gb_tb .gb_z,.gb_ub .gb_z{position:absolute;right:1px}.gb_z.gb_1,.gb_vb.gb_1,.gb_0a.gb_1{-webkit-box-flex:0;-webkit-flex:0 1 auto;flex:0 1 auto}.gb_wb.gb_xb .gb_ob{width:30px!important}.gb_P{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_yb .gb_P,.gb_zb .gb_P{right:0;top:0}.gb_Ha a.gb_Va{border-radius:100px;background:#0b57d0;background:var(--gm3-sys-color-primary,#0b57d0);box-sizing:border-box;color:#fff;color:var(--gm3-sys-color-on-primary,#fff);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_Ha a.gb_Wa{border-radius:100px;border:1px solid;border-color:#747775;border-color:var(--gm3-sys-color-outline,#747775);background:none;box-sizing:border-box;color:#0b57d0;color:var(--gm3-sys-color-primary,#0b57d0);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_1a.gb_H a.gb_Va,.gb_2a.gb_H a.gb_Va,.gb_3a.gb_H a.gb_Va{background:#c2e7ff;background:var(--gm3-sys-color-secondary-fixed,#c2e7ff);color:#001d35;color:var(--gm3-sys-color-on-secondary-fixed,#001d35)}.gb_Ha.gb_H a.gb_Wa{color:#a8c7fa;color:var(--gm3-sys-color-primary,#a8c7fa)}.gb_Ha a.gb_Od{padding:10px 12px;margin:12px 16px 12px 10px;min-width:85px}@media (max-width:640px){.gb_Ha a.gb_Od{min-width:75px}}.gb_Ha,.gb_Dd{font-family:"Google Sans Text",Roboto,Helvetica,Arial,sans-serif;font-style:normal}.gb_Ha.gb_1a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a.gb_Pd{background:#fff;background:var(--og-bar-background,var(--gm3-sys-color-background,#fff))}.gb_Ha.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_1a a.gb_Z,.gb_Ha.gb_1a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_1a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}@media (forced-colors:active) and (prefers-color-scheme:dark){.gb_Ha svg,.gb_Ha.gb_1a svg,.gb_Ha.gb_H svg{color:white}}.gb_Ha.gb_H.gb_1a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:transparent}.gb_Ha.gb_H.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_1a a.gb_Z,.gb_Ha.gb_H.gb_1a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_1a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:#1f1f1f;background:var(--og-bar-background,var(--gm3-sys-color-background,#131314))}.gb_Ha.gb_2a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a.gb_Pd{background:#e9eef6;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#e9eef6))}.gb_Ha.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_2a a.gb_Z,.gb_Ha.gb_2a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_2a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_H.gb_2a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a.gb_Pd{background:#282a2c;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#282a2c))}.gb_Ha.gb_H.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_2a a.gb_Z,.gb_Ha.gb_H.gb_2a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_2a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_3a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a.gb_Pd{background:transparent}.gb_Ha.gb_3a .gb_pd.gb_qd,.gb_Ha.gb_3a a.gb_Z,.gb_Ha.gb_3a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a .gb_rd .gb_Qd,.gb_Ha.gb_3a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_3a.gb_H.gb_Pd{background:transparent}.gb_Ha.gb_3a.gb_H .gb_pd.gb_qd,.gb_Ha.gb_3a.gb_H a.gb_Z,.gb_Ha.gb_3a.gb_H span.gb_Z{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H .gb_rd .gb_Qd,.gb_Ha.gb_3a.gb_H .gb_id .gb_Qd{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H svg{color:white;color:var(--og-theme-color,white)}.gb_Ha a.gb_Z,.gb_Ha span.gb_Z{text-decoration:none}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-box-flex:1;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_ud{display:none}.gb_Ha.gb_9a .gb_pd{margin-bottom:0}.gb_rd.gb_sd .gb_pd{padding-left:4px}.gb_Ha.gb_9a .gb_td{position:relative;top:-2px}.gb_Ha{min-width:160px;position:relative}.gb_Ha.gb_ad{min-width:120px}.gb_Ha.gb_Rd .gb_Sd{display:none}.gb_Ha.gb_Rd .gb_Kd{height:56px}header.gb_Ha{display:block}.gb_Ha svg{fill:currentColor}.gb_Td{position:fixed;top:0;width:100%}.gb_Ud{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Vd{height:64px}.gb_Kd{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ha:not(.gb_9a) .gb_Kd{padding:8px}.gb_Ha:not(.gb_9a) .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Ha.gb_Xd .gb_Kd{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha .gb_Kd.gb_Ld.gb_Zd{min-width:0}.gb_Ha.gb_9a .gb_Kd{padding:4px;padding-left:8px;min-width:0}.gb_Ha.gb_9a .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Sd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_0d>.gb_Sd{display:table-cell;width:100%}.gb_rd{padding-right:25px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha.gb_9a .gb_rd{padding-right:14px}.gb_1d{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_1d>:only-child{display:inline-block}.gb_2d.gb_jd{padding-left:4px}.gb_2d.gb_3d,.gb_Ha.gb_Xd .gb_2d,.gb_Ha.gb_9a:not(.gb_Dd) .gb_2d{padding-left:0}.gb_Ha.gb_9a .gb_2d.gb_3d{padding-right:0}.gb_Ha.gb_9a .gb_2d.gb_3d .gb_Xa{margin-left:10px}.gb_jd{display:inline}.gb_Ha.gb_dd .gb_2d.gb_4d,.gb_Ha.gb_Dd .gb_2d.gb_4d{padding-left:2px}.gb_pd{display:inline-block}.gb_2d{box-sizing:border-box;height:48px;padding:0 4px;padding-left:5px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Dd{height:48px}.gb_Ha.gb_Dd{min-width:auto}.gb_Dd .gb_2d{float:right;padding-left:32px;padding-left:var(--og-bar-parts-side-padding,32px)}.gb_Dd .gb_2d.gb_5d{padding-left:0}.gb_6d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_a a,.gb_6c a{color:inherit}.gb_qd{text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_qd{opacity:1}.gb_7d{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}.gb_0{display:inline-block;padding-left:15px}.gb_0 .gb_Z{display:inline-block;line-height:24px;vertical-align:middle}.gb_8d{text-align:left}.gb_K{display:none}@media screen and (max-width:319px){.gb_Kd .gb_J{display:none;visibility:hidden}}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}.gb_S{display:none!important}.gb_jb{visibility:hidden}@media screen and (max-width:319px){.gb_Kd:not(.gb_Ld) .gb_J{display:none;visibility:hidden}}.gb_vd{display:inline-block;vertical-align:middle}.gb_wd .gb_R{bottom:-3px;right:-5px}@if (RTL_LANG){.gb_wd .gb_R{left:-5px}}.gb_vd:first-child{padding-left:0}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:50%;box-sizing:border-box;height:40px;width:40px}.gb_B,#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}x:-o-prefocus{border-bottom-color:#ccc}.gb_ma{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:0;top:54px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text;user-select:text}.gb_vd.gb_5a .gb_ma,.gb_5a.gb_ma{display:block}.gb_Ad{position:absolute;right:0;top:54px;z-index:-1}.gb_pb .gb_ma{margin-top:-10px}.gb_vd:first-child{padding-left:4px}.gb_Ha.gb_Bd .gb_vd:first-child{padding-left:0}.gb_Cd{position:relative}.gb_id .gb_Cd,.gb_Dd .gb_Cd{float:right}.gb_B{padding:8px;cursor:pointer}.gb_Fd button svg,.gb_B{border-radius:50%}.gb_vd{padding:4px}.gb_Ha.gb_Bd .gb_vd{padding:4px 2px}.gb_Ha.gb_Bd .gb_z.gb_vd{padding-left:6px}.gb_ma{z-index:991;line-height:normal}.gb_ma.gb_Id{left:0;right:auto}@media (max-width:350px){.gb_ma.gb_Id{left:0}}.gb_Jd .gb_ma{top:56px}.gb_z .gb_B{padding:4px}.gb_T{display:none}.gb_0a:not(.gb_Wd){position:relative}.gb_be::after{content:"";border:1px solid #202124;opacity:.13;position:absolute;top:4px;left:4px;border-radius:50%;width:30px;height:30px;box-sizing:content-box}.gb_Xa{box-sizing:border-box;cursor:pointer;display:inline-block;height:48px;overflow:hidden;outline:none;padding:7px 0 0 16px;vertical-align:middle;width:142px;border-radius:28px;background-color:transparent;border:1px solid;position:relative}.gb_Xa .gb_0a{width:32px;height:32px;padding:0}.gb_Xa .gb_R{bottom:-2px;right:-4px}.gb_1a .gb_Xa,.gb_2a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_1a.gb_H .gb_Xa,.gb_2a.gb_H .gb_Xa{border-color:#8e918f;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#8e918f))}.gb_3a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_3a.gb_H .gb_Xa{border-color:#e3e3e3;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_4a{display:inherit}.gb_Xa .gb_4a{background:#fff;border-radius:6px;display:inline-block;left:15px;position:static;padding:2px;top:-1px;height:32px;box-sizing:border-box;width:78px}.gb_6a{text-align:center}.gb_6a.gb_7a{background-color:#f1f3f4}.gb_6a .gb_8a{vertical-align:middle;max-height:28px;max-width:74px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:0;margin-right:9px;float:right}.gb_Ha:not(.gb_9a) .gb_Xa{margin-left:10px;margin-right:4px}.gb_Xa .gb_be::after{left:0;top:0}@media screen and (max-width:480px){.gb_Xa .gb_4a{display:none}.gb_Xa{border:none;border-radius:50%;height:40px;margin:4px;outline:1px solid transparent;padding:0;width:40px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:4px;margin-right:0}}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US._dvPeXVR4X8.2019.O","com.co","es-419","425",0,[4,2,"","","","887809888","0"],null,"fADIaZC7OdbCwN4Pg96H-AI",null,0,"og.qtm.vjyYcS7rQwo.L.W.O","AA2YrTvQIrBtmHXP3htpEvFzVPlOIRB02Q","AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww","",2,1,200,"COL",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","glorgiib.gegi@gmail.com","","ADUjzeEUKy6Jq9HbCfhiRuGX-othREsKff7TBn9rsW1D-dOWx3FHziTjV1KHuvxN1mwFzbUswxqbnZ5haSSCtFuYNjn9TU9wiQ",0,0,null,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (predeterminado)","Cuenta de marca",1,"%1$s (delegado)",1,null,83,"https://colab.research.google.com/drive/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=es-419\u0026ts=250",0,"dashboard",null,null,null,null,"Perfil","",1,null,"Saliste de tu cuenta","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Quitar","Acceder",0,1,1,0,1,1,0,null,null,null,"Finalizó la sesión",null,null,null,"Visitante",null,"Predeterminado","Delegada","Salir de todas las cuentas",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","es-419"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.5G9F9JPGjf8.O/d=1/rs=AHpOoo-OYuAVGK84U6cg5lkjGc85qYpeMw/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20260309.0_p0","es-419",null,0],[0.009999999776482582,"com.co","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"COL","es-419","887809888.0",8,null,1,0,null,null,null,null,"3700949,105109531,105109534,105140909,105140912,115517798,115517801,116249040,116249043",null,null,null,"fADIaZC7OdbCwN4Pg96H-AI",0,0,0,null,2,5,"nn",138,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US._dvPeXVR4X8.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTvQIrBtmHXP3htpEvFzVPlOIRB02Q"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.vjyYcS7rQwo.L.W.O/m=qcwid,qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026amb=1\u0026dpi=114591953"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=es-419\u0026continue=https://colab.research.google.com/drive/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Se produjo un error.%1$s Actualiza la página para volver a intentarlo o %2$selige otra cuenta%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Alerta de seguridad crítica","Alerta importante de la cuenta","Alerta de uso del almacenamiento",null,1,1,0,0,"Alerta de la cuenta",0],null,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"es-419",0,["https://colab.research.google.com/drive/?authuser=$authuser","https://accounts.google.com/AddSession?hl=es-419\u0026continue=https://colab.research.google.com/drive/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=es-419\u0026continue=https://colab.research.google.com/drive/\u0026timeStmp=1774715004\u0026secTok=.AG5fkS9K0i7W929_0ePJEGbNREeMZy2QUA\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=es-419\u0026ts=250",0,0,"",0,0,null,0,null,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"1184720131",3,1,0,0],0,null,null,null,1,0,"glorgiib.gegi@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,Za,bb,db,ib,eb,kb,qb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Dk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.ha[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Qa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Ra=function(a){return a==null||typeof a==="string"?a:void 0};
_.Ua=function(a,b,c){if(a!=null&&a[_.Sa]===_.Ta)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Xa=function(a){const b=_.Va(_.Wa);return b?a[b]:void 0};Za=function(a,b){b<100||_.Ja(Ya,1)};
bb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Va(_.Wa),g;!e&&f&&(g=a[f])&&g.Ad(Za);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=$a)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const E=r-p;var q=void 0;((q=b)!=null?q:b={})[E]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let E;if(m&&!Number.isNaN(h)&&(E=h+p)<g)f[E]=q;else{let O;((O=b)!=null?O:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Va(_.Wa)&&(a=_.Xa(a))&&"function"==typeof _.ab&&a instanceof _.ab&&(f[_.Wa]=a.i());return f};
db=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.cb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:bb(a,b,db)}if(a!=null&&a[_.Sa]===_.Ta)return eb(a);if("function"==typeof _.fb&&a instanceof _.fb)return a.j();return}return a};ib=function(a,b){if(b){$a=b==null||b===Fa||b[gb]!==hb?Fa:b;try{return eb(a)}finally{$a=void 0}}return eb(a)};
eb=function(a){a=a.ha;return bb(a,a[_.v]|0,db)};
_.lb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(jb&&1&e)throw Error("m");2048&e&&!(2&e)&&kb();if(e&256)throw Error("n");if(e&64)return(e|d)!==e&&(a[_.v]=e|d),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<g)c[f+
b]=k[h],delete k[h];else break;e=e&-16760833|(g&1023)<<14;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-16760833|(h&1023)<<14}}}a[_.v]=e|64|d;return a};kb=function(){if(jb)throw Error("p");_.Ja(mb,5)};
qb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.nb(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Sa]===_.Ta)return b=a.ha,c=b[_.v]|0,_.Ea(a,c)?a:_.ob(a,b,c)?_.pb(a,b):_.nb(b,c);if("function"==typeof _.fb&&a instanceof _.fb)return a};_.pb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.nb=function(a,b,c,d){d!=null||(d=!!(34&b));a=bb(a,b,qb,d);d=32;c&&(d|=2);b=b&16769217|d;a[_.v]=b;return a};_.rb=function(a){const b=a.ha,c=b[_.v]|0;return _.Ea(a,c)?_.ob(a,b,c)?_.pb(a,b,!0):new a.constructor(_.nb(b,c,!1)):a};_.sb=function(a){if(a.j!==Da)return!1;var b=a.ha;b=_.nb(b,b[_.v]|0);b[_.v]|=2048;a.ha=b;a.j=void 0;a.o=void 0;return!0};_.tb=function(a){if(!_.sb(a)&&_.Ea(a,a.ha[_.v]|0))throw Error();};_.ub=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.ob=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.wb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>14&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.yb=function(a,b,c,d,e){let f=!1;d=_.xb(a,d,e,g=>{const h=_.Ua(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.ub(a,b),d};_.zb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(){this.qa=this.qa;this.Y=this.Y};_.Ab=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};
Db=Object.defineProperty;Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};
Gb("globalThis",function(a){return a||Fb});Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Va=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.vk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>18&1),Qb=!!(Kb[0]&8192),Rb=!!(Kb[0]>>20&1),Sb=!!(Kb[0]&512);var na=Pb?Rb:Jb(610401301,!1),jb=Pb?Qb||!Sb:Jb(748402147,!0);_.Tb=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Wb,Ub,Xb,Vb;_.cb=_.ba(a=>fa?a>=Ub&&a<=Vb:a[0]==="-"?ja(a,Wb):ja(a,Xb));Wb=Number.MIN_SAFE_INTEGER.toString();Ub=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Xb=Number.MAX_SAFE_INTEGER.toString();Vb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Yb=typeof TextDecoder!=="undefined";_.Zb=typeof TextEncoder!=="undefined";var oa,$b=_.t.navigator;oa=$b?$b.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.ac=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.bc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.cc=function(a){_.cc[" "](a);return a};_.cc[" "]=function(){};var qc;_.dc=_.ra();_.ec=_.sa();_.fc=_.u("Edge");_.hc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.ic=_.ma()&&!_.u("Edge");_.jc=_.za();_.kc=wa()?oa.platform==="Windows":_.u("Windows");_.lc=wa()?oa.platform==="Android":_.u("Android");_.mc=xa();_.nc=_.u("iPad");_.oc=_.u("iPod");_.pc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.hc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.fc)return/Edge\/([\d\.]+)/.exec(c);if(_.ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.ic)return/WebKit\/(\S+)/.exec(c);if(_.dc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ec){var rc;const c=_.t.document;rc=c?c.documentMode:void 0;if(rc!=null&&rc>parseFloat(a)){qc=String(rc);break a}}qc=a}_.sc=qc;_.tc=_.ta();_.uc=xa()||_.u("iPod");_.vc=_.u("iPad");_.wc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.xc=ua();_.yc=_.va()&&!_.ya();var Ya,mb,gb;_.Wa=_.Ca();_.zc=_.Ca();Ya=_.Ca();_.Ac=_.Ca();mb=_.Ca();_.Sa=_.Ca("m_m",!0);gb=_.Ca();_.Bc=_.Ca();var Dc;_.v=_.Ca("jas",!0);Dc=[];Dc[_.v]=7;_.Cc=Object.freeze(Dc);var Da;_.Ta={};Da={};_.Ec=Object.freeze({});var hb={};var Ia=void 0;_.Fc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Gc=Number.isSafeInteger;_.Na=Number.isFinite;_.Hc=Math.trunc;var $a;_.Ic=_.ia(0);_.Jc={};_.Kc=function(a,b,c,d,e){b=_.xb(a.ha,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.xb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Lc=function(a,b,c,d){_.tb(a);const e=a.ha;_.wb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.ha,f=e[_.v]|0;b=_.yb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.rb(b);g!==b&&(_.sb(a)&&(e=a.ha,f=e[_.v]|0),b=g,f=_.wb(e,f,c,b,d),_.ub(e,f))}return b};_.D=function(a,b,c){c==null&&(c=void 0);_.Lc(a,b,c);c&&!_.Ea(c)&&_.ub(a.ha);return a};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Kc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Ra(_.Kc(a,b,d)))!=null?e:c};_.H=function(a,b,c){return _.Ra(_.Kc(a,b,c,_.Jc))};
_.J=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Lc(a,b,c==null?c:_.Pa(c))};_.L=function(a,b,c,d){return _.Lc(a,b,_.Qa(c),d)};_.M=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.Oa(c),d)};_.N=class{constructor(a,b,c){this.ha=_.lb(a,b,c,2048)}toJSON(){return ib(this)}wa(a){return JSON.stringify(ib(this,a))}};_.N.prototype[_.Sa]=_.Ta;_.N.prototype.toString=function(){return this.ha.toString()};_.Mc=_.zb();_.Nc=_.zb();_.Oc=_.zb();_.Pc=Symbol();var Qc=class extends _.N{constructor(a){super(a)}};_.Sc=class extends _.N{constructor(a){super(a)}D(a){return _.K(this,3,a)}};_.Tc=class extends _.N{constructor(a){super(a)}};_.x.prototype.qa=!1;_.x.prototype.isDisposed=function(){return this.qa};_.x.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.x.prototype[Symbol.dispose]=function(){this.dispose()};_.x.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Uc=class extends _.x{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}yb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].yb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Wc=class extends _.x{constructor(){var a=_.Vc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Xc=class extends _.N{constructor(a){super(a)}};var Yc=class extends _.N{constructor(a){super(a)}};var ad;_.Zc=function(a,b,c=98,d=new _.Sc){if(a.i){const e=new Qc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.M(e,5,1);_.D(d,40,e);a.i.log(c,d)}};ad=class{constructor(){var a=$c;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Sc){_.Zc(this,a,98,c)}};var bd,cd;bd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.ac(c,b,a)}catch(d){console.error(d)}}}};_.dd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new cd(a,b,c));bd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;bd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;bd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
cd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.ed=a=>{var b="uc";if(a.uc&&a.hasOwnProperty(b))return a.uc;b=new a;return a.uc=b};_.P=class{constructor(){this.v=new _.dd;this.i=new _.dd;this.D=new _.dd;this.B=new _.dd;this.C=new _.dd;this.A=new _.dd;this.o=new _.dd;this.j=new _.dd;this.F=new _.dd;this.G=new _.dd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.ed(_.P)}};var hd;_.gd=function(){return _.C(_.fd,_.Tc,5)};hd=class extends _.N{constructor(a){super(a)}};var id;window.gbar_&&window.gbar_.CONFIG?id=window.gbar_.CONFIG[0]||{}:id=[];_.fd=new hd(id);var $c;$c=_.C(_.fd,Yc,3)||new Yc;_.Vc=new ad;_.A("gbar_._DumpException",function(a){_.Vc?_.Vc.log(a):console.error(a)});_.jd=new Wc;var ld;_.md=function(a,b){var c=_.kd.i();if(a in c.i){if(c.i[a]!=b)throw new ld;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.kd=class{constructor(){this.i={};this.j={}}static i(){return _.ed(_.kd)}};_.nd=class extends _.aa{constructor(){super()}};ld=class extends _.nd{};_.A("gbar.A",_.dd);_.dd.prototype.aa=_.dd.prototype.then;_.A("gbar.B",_.P);_.P.prototype.ba=_.P.prototype.qa;_.P.prototype.bb=_.P.prototype.O;_.P.prototype.bd=_.P.prototype.P;_.P.prototype.bf=_.P.prototype.K;_.P.prototype.bg=_.P.prototype.M;_.P.prototype.bh=_.P.prototype.L;_.P.prototype.bj=_.P.prototype.Y;_.P.prototype.bk=_.P.prototype.J;_.P.prototype.bl=_.P.prototype.N;_.A("gbar.a",_.P.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var od=new Uc;_.md("api",od);
var pd=_.gd()||new _.Tc,qd=window,rd=_.y(_.H(pd,8));qd.__PVT=rd;_.md("eq",_.jd);
}catch(e){_._DumpException(e)}
try{
_.sd=class extends _.N{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var td=class extends _.N{constructor(a){super(a)}};var ud=class extends _.x{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.H(a,1));_.Ma(_.Kc(a,12))!=null&&(d.dpo=_.Ab(_.F(a,12)));d.ms=_.y(_.H(a,2));d.m=_.y(_.H(a,3));d.l=[];_.G(b,1)&&(a=_.H(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.H(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var vd=_.C(_.fd,_.Xc,14);if(vd){var wd=_.C(_.fd,_.sd,9)||new _.sd,xd=new td,yd=new ud;yd.init(vd,wd,xd);_.md("gs",yd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_glorgiib.gegi@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./app.ipynb_files/bundle.css"><script nonce="">var colabVersionTag = 'colab-external_20260326-060108_RC01_890055500'; var colabScsVersion = '6536405d54f47e30398fd7ddd41f3ced'; var hl = 'es-419'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_prompt_cell\x22: true, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_user_input_char_limit\x22: 100000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_subpaths_in_kernel_url\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22assign_ping_hostname\x22: \x22https:\/\/ping.prod.colab.dev\x22, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22, \x22*.proxy.googlers.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_client_events_context\x22: true, \x22composer_compaction_interval\x22: 0, \x22composer_compaction_overlap_size\x22: 0, \x22composer_context_max_variable_length\x22: 500000, \x22composer_custom_context\x22: false, \x22composer_default_dock_right\x22: true, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_generated_cell_placement_logic\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_replace_empty_cells_when_adding_new_cells\x22: false, \x22composer_show_debug_info\x22: false, \x22composer_show_single_diff_buttons\x22: false, \x22composer_suggestion_chips_in_chat\x22: true, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22connect_enterprise_vm\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22critique_comments\x22: false, \x22data_inspector\x22: true, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_agent_pending_markdown_network_requests\x22: true, \x22drop_chat_links\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22edu_promotion_banner\x22: false, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_bigquery_data_explorer\x22: false, \x22enable_colab_mcp_integration\x22: true, \x22enable_colab_mcp_showdiff\x22: false, \x22enable_composer_changeset_plan_stacking\x22: true, \x22enable_composer_code_report\x22: false, \x22enable_composer_floating_spark_off\x22: false, \x22enable_composer_fp_orcas_integration\x22: false, \x22enable_composer_fp_orcas_integration_v2\x22: false, \x22enable_composer_g_4_g_models\x22: true, \x22enable_composer_generated_cell_insertion_position\x22: false, \x22enable_composer_suggestion_chips\x22: true, \x22enable_composer_text_cell_transformations\x22: true, \x22enable_dsa_agent_steps_bundle\x22: false, \x22enable_fp_user_provided_context_links\x22: false, \x22enable_g_4_g_as_default_model\x22: true, \x22enable_gcp_preferences\x22: false, \x22enable_iframe_unloading\x22: true, \x22enable_improved_composer_context_mentions\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_prism_mode\x22: false, \x22enable_rt_on_create\x22: false, \x22enable_vscode_telemetry\x22: true, \x22enable_web_mcp\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22homepage\x22: false, \x22hrc\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: true, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_assignments\x22: true, \x22migrate_ccu_info\x22: true, \x22migrate_delete_assignment\x22: false, \x22migrate_tfe_keep_alive\x22: true, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22optimize_composer_context_order\x22: false, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22pds_minting\x22: false, \x22preference_deep_equality_check\x22: true, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_composer_planning_overeagerness\x22: true, \x22refresh_warning_timeout_ms\x22: 604800000, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: true, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: false, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222026.01\x22, \x222025.10\x22, \x222025.07\x22\x5d, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22snippets_ui_refresh\x22: false, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_timeout_ms\x22: 300000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22trim_filename_extension\x22: false, \x22truncate_composer_execution_results\x22: true, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_kernel_state_metadata_adk\x22: false, \x22use_kkb_if_configured\x22: false, \x22use_refactored_constraints\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22G4\x22, \x22H100\x22, \x22L4\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_composer_tools\x22: \x5b\x5d, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22vscode_test_feature\x22: \x22prod\x22, \x22want_completions_ai_consent_campaign\x22: true, \x22ids\x22: \x5b20730457, 20730556, 20730652, 20730660, 20730705, 20730183, 20730640, 20730644, 20730688, 20730559, 20730547, 20730460\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22assign_ping_hostname\x22: 45747049, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_client_events_context\x22: 45729342, \x22composer_compaction_interval\x22: 45749782, \x22composer_compaction_overlap_size\x22: 45749781, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_custom_context\x22: 45728743, \x22composer_default_dock_right\x22: 45755037, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_generated_cell_placement_logic\x22: 45721730, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_replace_empty_cells_when_adding_new_cells\x22: 45788233, \x22composer_show_debug_info\x22: 45700003, \x22composer_show_single_diff_buttons\x22: 45723066, \x22composer_suggestion_chips_in_chat\x22: 45757782, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22connect_enterprise_vm\x22: 45730782, \x22converse_notebook_context_length\x22: 45705427, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_agent_pending_markdown_network_requests\x22: 45768013, \x22drop_chat_links\x22: 45646864, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22edu_promotion_banner\x22: 45740730, \x22embedded_use_websockets\x22: 45691694, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_bigquery_data_explorer\x22: 45765771, \x22enable_colab_mcp_integration\x22: 45741279, \x22enable_colab_mcp_showdiff\x22: 45768032, \x22enable_composer_changeset_plan_stacking\x22: 45744296, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_floating_spark_off\x22: 45771195, \x22enable_composer_fp_orcas_integration\x22: 45744285, \x22enable_composer_fp_orcas_integration_v2\x22: 45758361, \x22enable_composer_g_4_g_models\x22: 45745479, \x22enable_composer_generated_cell_insertion_position\x22: 45763491, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_composer_text_cell_transformations\x22: 45758370, \x22enable_dsa_agent_steps_bundle\x22: 45755666, \x22enable_fp_user_provided_context_links\x22: 45746774, \x22enable_g_4_g_as_default_model\x22: 45745683, \x22enable_gcp_preferences\x22: 45762481, \x22enable_iframe_unloading\x22: 45765934, \x22enable_improved_composer_context_mentions\x22: 45721452, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_prism_mode\x22: 45765531, \x22enable_rt_on_create\x22: 45667583, \x22enable_vscode_telemetry\x22: 45760437, \x22enable_web_mcp\x22: 45769687, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22homepage\x22: 45769473, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_assignments\x22: 45752830, \x22migrate_ccu_info\x22: 45716751, \x22migrate_delete_assignment\x22: 45760675, \x22migrate_tfe_keep_alive\x22: 45766773, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22optimize_composer_context_order\x22: 45759155, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22pds_minting\x22: 45648255, \x22preference_deep_equality_check\x22: 45740961, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_composer_planning_overeagerness\x22: 45758628, \x22refresh_warning_timeout_ms\x22: 45765093, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22snippets_ui_refresh\x22: 45737461, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22trim_filename_extension\x22: 45691676, \x22truncate_composer_execution_results\x22: 45746694, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_kernel_state_metadata_adk\x22: 45737477, \x22use_kkb_if_configured\x22: 45733350, \x22use_refactored_constraints\x22: 45740233, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_composer_tools\x22: 45752901, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22vscode_test_feature\x22: 45755614, \x22want_completions_ai_consent_campaign\x22: 45671138\x7d\x7d'); var colabUserEmail = 'glorgiib.gegi@gmail.com'; var colabRenderDataToken = 'AFWLbD2TF6pmNMTCFbAYaooGvkmpoq5v1I_xkSuht_vjpA-F2QwxNo_v5P-HOFeeui_GAuDEEjVTWqHJnfbK9Rzdp41hh04myLjXCpECjBus6ovAmuGuvg\x3d\x3d'; var colabConfig = '\x5b\x5b\x22glorgiib.gegi@gmail.com\x22,\x5b1,\x22AHXL0D22YlNLVn2id3t5HZWJXZeT1aFO9mCoSJRbeGdgm3rVrURKZRF8hs2f0OP+BpwEQL07kGMv\/JpTW6zpcCfUj0eHde+B36j+\/pKKglM3yjGNYAXU2U8KytQnASrx2SLqZrjXL8NuSQKVcl8mhoGK40iAT58N0nN\/OjTRk8MV9xJUA\/CmbhINrawMbIRK7NM8PmtHK5GLd+i4RtyuZKS2RMlGVH8f05LI6DvfWNXvcb5pF\/6\/AAUHgiZYe9sv0CGXdl7zYjQ4WKygAgIHrOaGk3SLkNEA\/nSjrtlrmxXrfduGTwKO7yF6fmz9bIpMVZh1GmFaMcJCxarau3GPPTeXrldwxN3tqwQ4qpa0ayPRXWChAiN\/A7KqmNFMe+qm4G4KOhutLWVjWLgxytdglA50Go0imdsLQME1c8sqR7wUI8TEB4ao2aXAVnYVgU9h3ov5XgbFGDLiYap3uMxfYVOqof91m3oknHwMR7auKDwRi9gAB0cgaeGsdJYyRh7UFEGjENMgqaW2F\/JJ1daoTmy3fz7E+QzUfXI3GePhCBvMXsjvDozl2FELx142qXwlnlCJx30UCIHwxWoiMR9j3GelHHDBT\/x+RWy2nxDua1qkJ4QuDuNwE+tNGp66\/eAM1EhjN2sC4ozAPHq6+csVIuyjaeH2X+soOj2aamlrYqGfwddVJ+kp1ky2o9CQESCJcaMsJKxRirGjxjKEQgjzm3aXTdClGbhNHQBGoMikEi02JzyA2BesH2UwSvVNMJ3nP77GelIaa69uRGsRXn0S+MpBJHqt2yTMpj8zAF2P05eCqtI10gR0l6T+ThJ3HI+MHYEaMmhpxjeSpvEqv8h0mEexVdHjlFeLZBTCTdPZbDjfsxIQzCiKLqW1D0MdILAwFC\/14LgjyQOVlFDFDWBQL5+r7qTAKAqk1XgLXT6iQ9XcPNxqW3bv5igXcd6HteAR8vB+T5saItzXU1\/my1A+5hFKlzB66SRBfnb28zXis9SI9uY8SootQ+A9WdZmJh9DkfNlfrrQyrJvRmRKa4ZHBHu0w7uGPcSLXie2QgWIPkt70\/1oso9wyXcKFLJh\/SeJEdLxIZbPon+ubH6c\/HHqecEKkD5lJ3hBElyQKbQ74kygj7rwJUyZpdmRIrhElvrGdnJh2Mpeqj\/qWadRhgMrtUtxhDrMdNccUJd2xzp8y9q+J+6PqotFk1z6ukn2JyP8UD4J\/lHQyaQvYBLn4Qh3EJfkolD5s23zItgyhg9bixU2r3mBmggSFr\/J1tN0GXQazHDLFArTsSQj0voofL+jAQavtCxJMCHkKg8mR1pRwcUO+te2z1tj9wn5B8ECTqo+LdLTy6SqiD4hTepUNNzA2FASYPXtwPy+LPhXqYARBq+6VpA0i2Wv2YKhCgoX6g\/j12QI7ad\/EScvPBlnvn7AunpmBIKParua7Yb3Xb7MVIgypV03QLX5gESF\/GgOR6quKeA1AJJJFvA0cxwbMr2S0o2rVYwilH+G5j1ioR9DRFhbKVhZral\/grlTWdULT5mJq3Yomx+QtiUDMGUYifcySjOcd9ve6plxP\/vUTU+parsvHpU9ku3goB6VcmRDLXYo3ZwFaafbw4R53OatZtu8heiplBvboPrT85K89MaW6q2k8lWTGiHt2KuXk6tym9nxZZ3ZyGUAKsS1XZaPLD2R7irgA36ncsCQP6UJ8hxZ3vXQap8x9EzU36TorGWR711hEB9D2GsISK\/rXVDAVE8Z6EfYmPgBvC15oWltuB7i2tDYP\/NhMk5dxQVf79jAQcSZ+vXCK9pbk0YDQU5opqqTo6S6ZlVJTlZZpBbhOpapRwUpXoAIkotxddhK7WdZ1L3jEo8UPI+kBnIEdUAi2AxxYuaZzWXFLlfKKUiQ6o972GAg4wQQjLXzZuZvmCY4tMEnae9oDqPAW3x79Rmu8zgpdj9A9Ey\/n6Yzsnn6JFRxOncyC8ihVqzdmoge1ZQKyvWZZxjR91zUN2fgfQidoLyT3GlVK0Z27hLg0Bcun0bBLcQZkMWtT4WISEmOeCk+9KLIbBLSsY1zo84U4anE80iLoUqYdfyJTADcqsqdVRRNiwsttEusmYP2GIY\x3d\x22,\x22AJ9oCCykexj9sN6k4fhqrL5hVSCP8tR7FHPjReiFTE8qhyXvtk5iron7nvzE8fcPfzU5SdVkqjM44LDXQkmaH+aPT\/ZDGTINSJaDXfEXaeFZXPqApecjPIc6Fp2zMwUCjTWBRphQW17V\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$ 43.164,87\x22,\x22$ 215.995,71\x22,\x22$ 43.164,87\x22,\x22$ 215.995,71\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22CO\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/6536405d54f47e30398fd7ddd41f3ced/img%2Ffavicon_error.ico"><meta name="google-site-verification" content="h4AyILcMXlXf3PDJKg3Fu2_dyS3jfH5im5G__oDgjOs"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="gl3hNNVi7GnXImkDiRAkUxkhUD4g7Ke8L4D6Ve8FEVY"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="HwWGKCyRK7kxGyAlA30sbbTly9VW0SOM7Sh4juqiOVA"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./app.ipynb_files/lazy.min.js" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./app.ipynb_files/rs=AA2YrTvQIrBtmHXP3htpEvFzVPlOIRB02Q" nonce=""></script><link type="text/css" href="./app.ipynb_files/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 5px 0px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 5px; -webkit-border-radius: 5px; -moz-border-radius: 5px; -khtml-border-radius: 5px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 1px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: .7em}
.MathJax_MenuRadioCheck.RTL {right: .7em; left: auto}
.MathJax_MenuLabel {padding: 1px 2em 3px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #DDDDDD; margin: 4px 3px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: #606872; color: white}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./app.ipynb_files/editor.main.js"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./app.ipynb_files/editor.main.css"><script async="async" type="text/javascript" src="./app.ipynb_files/editor.main.nls.js"></script><script src="./app.ipynb_files/api.js" nonce=""></script><script src="./app.ipynb_files/api(1).js" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #282a2c; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #282a2c;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #282a2c;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #282a2c;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #282a2c;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #282a2c;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #282a2c; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script async="async" type="text/javascript" src="./app.ipynb_files/markdown.js"></script><script async="async" type="text/javascript" src="./app.ipynb_files/python.js"></script></head><body class="" data-new-gr-c-s-check-loaded="14.1279.0" data-gr-ext-installed="" data-new-gr-c-s-loaded="14.1279.0" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./app.ipynb_files/gapi_loader.js" nonce=""></script><script src="./app.ipynb_files/socketio_binary.js" nonce=""></script><script src="./app.ipynb_files/MathJax.js" nonce=""></script><script src="./app.ipynb_files/js_monaco_editor_vs_loader.js" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./app.ipynb_files/external_binary_l10n__es_419.js" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$019689205$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$019689205$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Cerrar" data-aria-label="Cerrar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$019689205$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$019689205$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Cargando…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Cerrar" data-aria-label="Cerrar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_T" ng-non-bindable=""><div class="gb_Rc"><div>Cuenta&nbsp;de&nbsp;Google</div><div class="gb_g">Gloria Gil Ibarra</div><div>glorgiib.gegi@gmail.com</div><div class="gb_Sc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Jd;Jd=class extends _.nd{};_.Kd=function(a,b){if(b in a.i)return a.i[b];throw new Jd;};_.Ld=function(a){return _.Kd(_.kd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Od;_.Md=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Od=function(a){return new _.Nd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Pd=globalThis.trustedTypes;_.Qd=class{constructor(a){this.i=a}toString(){return this.i}};_.Rd=new _.Qd("about:invalid#zClosurez");_.Nd=class{constructor(a){this.Vh=a}};_.Sd=[Od("data"),Od("http"),Od("https"),Od("mailto"),Od("ftp"),new _.Nd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Td=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Ud=new _.Td(_.Pd?_.Pd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Zd,ke,ne,Yd,$d,ee;_.Vd=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Wd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Xd=function(a,b){return a.lastIndexOf(b,0)==0};Zd=function(){let a=null;if(!Yd)return a;try{const b=c=>c;a=Yd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.ae=function(){$d===void 0&&($d=Zd());return $d};
_.ce=function(a){const b=_.ae();a=b?b.createScriptURL(a):a;return new _.be(a)};_.de=function(a){if(a instanceof _.be)return a.i;throw Error("x");};_.fe=function(a){if(ee.test(a))return a};_.ge=function(a){if(a instanceof _.Qd)if(a instanceof _.Qd)a=a.i;else throw Error("x");else a=_.fe(a);return a};_.he=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};
_.ie=function(a,b,c,d){return _.Vd(_.Kc(a,b,c,d))};_.Q=function(a,b,c){return _.Ma(_.Kc(a,b,c,_.Jc))};_.je=function(a,b){return _.Wd(_.Kc(a,b,void 0,_.Jc))};ke=class extends _.N{constructor(a){super(a)}Yb(a){return _.L(this,24,a)}};_.le=function(){return _.C(_.fd,ke,1)};_.me=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Yd=_.Pd;_.be=class{constructor(a){this.i=a}toString(){return this.i+""}};ee=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var te,xe,oe;_.qe=function(a){return a?new oe(_.pe(a)):ne||(ne=new oe)};_.re=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.se(c,"*",a,b)[0]||null);return a||null};_.se=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.ue=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:te.hasOwnProperty(d)?a.setAttribute(te[d],c):_.Xd(d,"aria-")||_.Xd(d,"data-")?a.setAttribute(d,c):a[d]=c})};te={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ve=function(a){return a?a.defaultView:window};_.ye=function(a,b){const c=b[1],d=_.we(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ue(d,c));b.length>2&&xe(a,d,b);return d};xe=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.me(f)||_.Lb(f)&&f.nodeType>0?d(f):_.ac(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Md(f):f,d)}};
_.ze=function(a){return _.we(document,a)};_.we=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.Ae=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.Be=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.Ce=function(a,b){return a&&b?a==b||a.contains(b):!1};_.pe=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};oe=function(a){this.i=a||_.t.document||document};_.n=oe.prototype;
_.n.H=function(a){return _.re(this.i,a)};_.n.Ra=function(a,b,c){return _.ye(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Pe=_.Ae;_.n.tg=_.Be;_.n.rg=_.Ce;
}catch(e){_._DumpException(e)}
try{
_.Mi=function(a){const b=_.he("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Oi=function(a){if(!a)return null;a=_.H(a,4);var b;a===null||a===void 0?b=null:b=_.ce(a);return b};_.Pi=function(a,b,c){a=a.ha;return _.yb(a,a[_.v]|0,b,c)!==void 0};_.Qi=class extends _.N{constructor(a){super(a)}};_.Ri=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Ti=function(a,b,c){a<b?Si(a+1,b):_.Vc.log(Error("W`"+a+"`"+b),{url:c})},Si=function(a,b){if(Ui){const c=_.ze("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.de(Ui);_.Mi(c);c.onerror=_.Ob(Ti,a,b,c.src);_.Ri("HEAD")[0].appendChild(c)}},Vi=class extends _.N{constructor(a){super(a)}};var Wi=_.C(_.fd,Vi,17)||new Vi,Xi,Ui=(Xi=_.C(Wi,_.Qi,1))?_.Oi(Xi):null,Yi,Zi=(Yi=_.C(Wi,_.Qi,2))?_.Oi(Yi):null,$i=function(){Si(1,2);if(Zi){const a=_.ze("LINK");a.setAttribute("type","text/css");a.href=_.de(Zi).toString();a.rel="stylesheet";let b=_.he("style",document);b&&a.setAttribute("nonce",b);_.Ri("HEAD")[0].appendChild(a)}};(function(){const a=_.le();if(_.Q(a,18))$i();else{const b=_.je(a,19)||0;window.addEventListener("load",()=>{window.setTimeout($i,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><scribe-shadow id="crxjs-ext" data-crx="okfkdaglfjjjfefdcppliegebpoegaii" style="position: fixed; width: 0px; height: 0px; top: 0px; left: 0px; z-index: 2147483647; overflow: visible; visibility: visible;"><template shadowrootmode="open"><div id="root-scribe-elem" style="position: fixed; width: 0px; height: 0px; top: 0px; left: 0px; overflow: visible; color: rgb(21, 24, 30);"><div role="region" aria-label="Notifications (F8)" tabindex="-1" style="pointer-events: none;"><ol class="fixed bottom-auto right-0 top-0 z-[999999] flex max-h-screen w-[400px] max-w-full p-4" tabindex="-1"></ol></div></div><link rel="stylesheet" href="chrome-extension://okfkdaglfjjjfefdcppliegebpoegaii/assets/style.css"></template></scribe-shadow><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: STIXSizeOneSym, sans-serif;"></div></div><iframe id="hfcr" src="./app.ipynb_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$019689205$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><a id="link" class="button" href="https://colab.research.google.com/drive/1T40YdV70LtqWwWloyBK1tI6t2ZYkAH3M#notebook-main"><!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </a>
    </template><!--?lit$019689205$-->Ir al contenido principal</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$019689205$-->
    <!--?lit$019689205$-->
          <div id="private-outputs-warning" hidden="" class="header-warning private-outputs-warning"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$019689205$-->El notebook se abrió con la configuración de resultados privados; estos no se guardarán. Puedes inhabilitar esta opción en la <a href="https://colab.research.google.com/drive/1T40YdV70LtqWwWloyBK1tI6t2ZYkAH3M#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">configuración del notebook</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Abrir la configuración del notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Cerrar" data-aria-label="Cerrar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$019689205$--> <!--?lit$019689205$-->
    <div hidden="" class="header-warning refresh-warning undismissible"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
      <div class="message"><!--?lit$019689205$-->Tu versión de Colab está desactualizada. Actualiza la página para acceder a las actualizaciones más recientes.</div>
      <div class="actions">
        <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <!--?lit$019689205$-->Actualizar para acceder
        </md-text-button>
      </div>
    </div>
  
    <!--?lit$019689205$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><div id="header-logo">
              <!--?lit$019689205$--><!--?lit$019689205$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="Ver en Google Drive">
        <!--?lit$019689205$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$--><svg viewBox="0 0 24 24"><!--?lit$019689205$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$019689205$--><!--?lit$019689205$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Bloc de notas almacenado en Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Nombre del notebook" command="rename" aria-describedby="doc-name-tooltip" style="width: 147.695px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cambiar el nombre del bloc de notas</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Despliegue.ipynb_</colab-input-sizer>
            <!--?lit$019689205$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Destacar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Destacar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Destacar notebook en Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$019689205$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="Se guardaron todos los cambios" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Se guardaron todos los cambios">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="Se guardaron todos los cambios"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Se guardaron todos los cambios</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" style="user-select: none;" tabindex="0" aria-activedescendant=":b"><!--?lit$019689205$--><div class="goog-menu-button goog-inline-block goog-menu-button-open" id="file-menu-button" role="button" aria-expanded="true" aria-haspopup="true" style="user-select: none;" aria-activedescendant=":b" aria-owns=":b"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Archivo</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Editar</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Ver</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Insertar</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Entorno de ejecución</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Herramientas</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$019689205$-->Ayuda</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$019689205$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$019689205$-->
      <!--?lit$019689205$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$019689205$--><md-icon-button id="comments" command="open-comments-thread" data-aria-label="Abrir panel de comentarios" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Abrir panel de comentarios">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Abrir panel de comentarios</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$019689205$--><md-icon-button id="settings-cog" command="preferences" data-aria-label="Abrir configuración" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Abrir configuración">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Abrir configuración</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$019689205$--><md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Compartir notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Compartir notebook">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->people</md-icon>
                <!--?lit$019689205$-->Compartir
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Compartir notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Activar o desactivar Gemini" aria-describedby="show-chat-button-tooltip" hidden="" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Activar o desactivar Gemini">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
            <!--?lit$019689205$-->Gemini
          </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Activar o desactivar Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ha gb_Dd gb_yb gb_e gb_3a gb_dd" id="gb"><div class="gb_2d gb_wb gb_Sd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Cd" style="display:block"><div class="gb_jd"></div><div class="gb_z gb_vd gb_Qf gb_1"><div class="gb_D gb_vb gb_Qf gb_1"><a class="gb_B gb_0a gb_1" aria-expanded="false" aria-label="Cuenta de Google: Gloria Gil Ibarra  
(glorgiib.gegi@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=es-419&amp;continue=https://colab.research.google.com/drive/&amp;ec=GBRAqQM" tabindex="0" role="button"><div class="gb_P"><svg focusable="false" height="40px" version="1.1" viewBox="0 0 40 40" width="40px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="opacity:1.0"><path d="M4.02,28.27C2.73,25.8,2,22.98,2,20c0-2.87,0.68-5.59,1.88-8l-1.72-1.04C0.78,13.67,0,16.75,0,20c0,3.31,0.8,6.43,2.23,9.18L4.02,28.27z" fill="#F6AD01"></path><path d="M32.15,33.27C28.95,36.21,24.68,38,20,38c-6.95,0-12.98-3.95-15.99-9.73l-1.79,0.91C5.55,35.61,12.26,40,20,40c5.2,0,9.93-1.98,13.48-5.23L32.15,33.27z" fill="#249A41"></path><path d="M33.49,34.77C37.49,31.12,40,25.85,40,20c0-5.86-2.52-11.13-6.54-14.79l-1.37,1.46C35.72,9.97,38,14.72,38,20c0,5.25-2.26,9.98-5.85,13.27L33.49,34.77z" fill="#3174F1"></path><path d="M20,2c4.65,0,8.89,1.77,12.09,4.67l1.37-1.46C29.91,1.97,25.19,0,20,0l0,0C12.21,0,5.46,4.46,2.16,10.96L3.88,12C6.83,6.08,12.95,2,20,2" fill="#E92D18"></path></svg></div><span class="gb_be"><img class="gb_Q gbii" src="./app.ipynb_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyiyAPYP2JtfeX1sWv4JMEvWi2Ix64d-wEtv8IN88OBakG12=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyiyAPYP2JtfeX1sWv4JMEvWi2Ix64d-wEtv8IN88OBakG12=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_R gb_S" aria-hidden="true"><svg class="gb_La" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ma" cx="7" cy="7" r="7"></circle><path class="gb_Oa" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.zd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.zd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Ad=document.querySelector(".gb_J .gb_B"),Bd=document.querySelector("#gb.gb_ad");Ad&&!Bd&&_.zd(_.jd,Ad,"click");
}catch(e){_._DumpException(e)}
try{
_.nh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ka()&&a.i[b].B())return a.i[b];return null};_.oh=function(a,b){a.i[b.J()]=b};var ph=new class extends _.x{constructor(){var a=_.Vc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.nh(this)&&_.nh(this).J()==a||this.i[a].P(!0))}Ua(a){this.j=a;for(const b in this.i)this.i[b].ka()&&this.i[b].Ua(a)}oc(a){return a in this.i?this.i[a]:null}};_.md("dd",ph);
}catch(e){_._DumpException(e)}
try{
_.Gi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Hi=document.querySelector(".gb_z .gb_B"),Ii=document.querySelector("#gb.gb_ad");Hi&&!Ii&&_.zd(_.jd,Hi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$019689205$-->
    <!--?lit$019689205$--><colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$019689205$--><span class="screenreader-only"><!--?lit$019689205$-->Mostrar paleta de comandos <!--?lit$019689205$-->⌘/Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$019689205$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Mostrar paleta de comandos" shortcut="⌘/Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar paleta de comandos (⌘/Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
          <!--?lit$019689205$-->Comandos
        </colab-toolbar-button>
    <!--?lit$019689205$--><span class="toolbar-add-code-split"><colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code" class=" split-button "><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$019689205$--><span class="screenreader-only"><!--?lit$019689205$-->Insertar celda de código abajo <!--?lit$019689205$-->⌘/Ctrl+M B</span>
      </md-text-button>
      <!--?lit$019689205$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insertar celda de código abajo" shortcut="⌘/Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar celda de código abajo (⌘/Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$019689205$-->Código
            </colab-toolbar-button>
            <!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" id="top-toolbar-add-code-dropdown-button" data-aria-label="Insertar celdas de código" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insertar celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="top-toolbar-add-code-dropdown-button" message="Insertar celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar celdas de código</div><!----><!--?--></template>
    </colab-tooltip-trigger></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$019689205$--><span class="screenreader-only"><!--?lit$019689205$-->Agregar celda de texto <!--?lit$019689205$--></span>
      </md-text-button>
      <!--?lit$019689205$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Agregar celda de texto" shortcut=""><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar celda de texto</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$019689205$-->Texto
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Ejecutar todas las celdas del bloc de notas"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$019689205$--><span class="screenreader-only"><!--?lit$019689205$-->Ejecutar todas las celdas del bloc de notas <!--?lit$019689205$--></span>
      </md-text-button>
      <!--?lit$019689205$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Ejecutar todas las celdas del bloc de notas" shortcut=""><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar todas las celdas del bloc de notas</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$019689205$-->Ejecutar todo
      </colab-toolbar-button>
      <!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="Más acciones" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="Más acciones"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$019689205$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$019689205$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$019689205$--><!----><md-menu-item command="restart" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item" tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Reiniciar la sesión</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item" tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Reiniciar la sesión y ejecutar todas las celdas</span>
  </md-menu-item><!----><!----><md-menu-item command="runafter" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Ejecutar la celda enfocada y todas las que se encuentran debajo</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item" tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Interrumpir la ejecución</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Borrar todos los resultados</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$019689205$-->
    <!--?lit$019689205$-->
    <!--?lit$019689205$-->
    <!--?lit$019689205$-->
    <!--?lit$019689205$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="Se guardaron todos los cambios" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Se guardaron todos los cambios">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="Se guardaron todos los cambios"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Se guardaron todos los cambios</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$019689205$-->
    <!--?lit$019689205$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$019689205$--><!--?--></template></colab-connect-warning-button>
    <!--?lit$019689205$--><!--?lit$019689205$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$019689205$--> <!--?lit$019689205$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Enfocar la última celda ejecutada" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Enfocar la última celda ejecutada">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Enfocar la última celda ejecutada"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Enfocar la última celda ejecutada</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Conectado a
del backend de Google Compute Engine en Python 3
RAM: 1.26 GB/12.67 GB
Disco: 21.20 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$019689205$--><span class="screenreader-only"><!--?lit$019689205$-->Conectado a
del backend de Google&nbsp;Compute&nbsp;Engine en Python 3
RAM: 1.26 GB/12.67 GB
Disco: 21.20 GB/107.72 GB <!--?lit$019689205$--></span>
      </md-text-button>
      <!--?lit$019689205$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Conectado a
del backend de Google Compute Engine en Python 3
RAM: 1.26 GB/12.67 GB
Disco: 21.20 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Conectado a</div><!----><!----><div><!--?lit$019689205$-->del backend de Google&nbsp;Compute&nbsp;Engine en Python 3</div><!----><!----><div><!--?lit$019689205$-->RAM: 1.26 GB/12.67 GB</div><!----><!----><div><!--?lit$019689205$-->Disco: 21.20 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$019689205$--> <div id="connect-button-resource-display">
          <!--?lit$019689205$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$019689205$-->RAM</div>
      <!--?lit$019689205$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
          <!--?lit$019689205$--><colab-usage-sparkline class="disks" label="Disco"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$019689205$-->Disco</div>
      <!--?lit$019689205$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        </div>
      </colab-toolbar-button>
      <!--?lit$019689205$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Otras opciones de conexión" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Otras opciones de conexión" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Otras opciones de conexión"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Otras opciones de conexión</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$019689205$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$019689205$-->
    <span class="collapsed-options">
      <!--?lit$019689205$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Compartir notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Compartir notebook">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Compartir notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Abrir configuración" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Abrir configuración">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Abrir configuración</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$019689205$-->
      <span class="colab-separator"></span>
    </span>
    <!--?lit$019689205$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" touch-target="none" data-aria-label="Activar o desactivar la visibilidad del encabezado" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activar o desactivar la visibilidad del encabezado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Activar o desactivar la visibilidad del encabezado</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$019689205$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Índice" title="Índice" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Índice" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="find" data-aria-label="Buscar y reemplazar" title="Buscar y reemplazar" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Buscar y reemplazar" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="snippets" data-aria-label="Fragmentos de código" title="Fragmentos de código" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fragmentos de código" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->code</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="show-data-inspector" data-aria-label="Inspector de datos" title="Inspector de datos" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Inspector de datos" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->eye_tracking</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="show-files" data-aria-label="Archivos" title="Archivos" value="" selected=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard selected" aria-label="Archivos" aria-pressed="true">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->folder</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$019689205$--><md-icon-button toggle="" command="show-data-explorer" data-aria-label="Explorador de datos" title="Explorador de datos" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Explorador de datos" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->table</md-icon>
    </md-icon-button> <!--?lit$019689205$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
            <!----> <!--?lit$019689205$-->
      <h3 class="left-pane-content-title"><!--?lit$019689205$-->Archivos</h3>
      <!--?lit$019689205$--> <!--?lit$019689205$-->
      <!--?lit$019689205$--><md-icon-button class="colab-left-pane-action colab-left-pane-move" data-aria-label="Mover panel izquierdo a una pestaña" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mover panel izquierdo a una pestaña">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </md-icon-button> <!--?lit$019689205$--><md-icon-button class="colab-left-pane-action colab-left-pane-close" data-aria-label="Cerrar panel izquierdo" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar panel izquierdo">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button><!--?--></div>
            <div class="left-pane-container"><colab-file-browser class="layout vertical"><colab-file-tree><!----> <!--?lit$019689205$-->
        <div class="file-tree-buttons">
          <label for="file-tree-upload-input">
            <md-icon-button class="colab-icon file-tree-upload-button" title="Carga archivos al almacenamiento de sesión" data-aria-label="Carga archivos al almacenamiento de sesión" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Carga archivos al almacenamiento de sesión">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
              <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload</md-icon>
            </md-icon-button>
          </label>
          <input id="file-tree-upload-input" type="file" multiple="">
          <md-icon-button class="file-tree-refresh" title="Actualizar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard ">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>refresh</md-icon>
          </md-icon-button>
          <md-icon-button toggle="" class="mount-drive-button" title="Activar unidad de Drive" data-aria-label="Activar unidad de Drive" aria-label-selected="Desactivar Drive" style="display: flex;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activar unidad de Drive" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$--><svg viewBox="0 0 24 24"><!--?lit$019689205$-->
    <path d="M17.2292 13.6042L15.5833 10.7917C15.5278 10.6944 15.4583 10.625 15.375 10.5833C15.2917 10.5278 15.1944 10.5 15.0833 10.5H13.9167C13.8056 10.5 13.7083 10.5278 13.625 10.5833C13.5417 10.625 13.4722 10.6944 13.4167 10.7917L11.7708 13.6042C11.7153 13.7014 11.6875 13.7986 11.6875 13.8958C11.6875 13.9931 11.7153 14.0903 11.7708 14.1875L12.3542 15.2083C12.4097 15.3056 12.4792 15.3819 12.5625 15.4375C12.6597 15.4792 12.7639 15.5 12.875 15.5H16.1458C16.2569 15.5 16.3542 15.4792 16.4375 15.4375C16.5208 15.3819 16.5903 15.3056 16.6458 15.2083L17.25 14.1875C17.3056 14.0903 17.3264 13.9931 17.3125 13.8958C17.3125 13.7986 17.2847 13.7014 17.2292 13.6042ZM13.5625 13.8333L14.5 12.1667L15.4375 13.8333H13.5625ZM5.5 18.5C5.09722 18.5 4.74306 18.3542 4.4375 18.0625C4.14583 17.7569 4 17.4028 4 17V7.5C4 7.08333 4.14583 6.72917 4.4375 6.4375C4.74306 6.14583 5.09722 6 5.5 6H10.4792L12 7.5H18.5C18.9167 7.5 19.2708 7.64583 19.5625 7.9375C19.8542 8.22917 20 8.58333 20 9V17C20 17.4028 19.8542 17.7569 19.5625 18.0625C19.2708 18.3542 18.9167 18.5 18.5 18.5H5.5ZM5.5 17H18.5V9H11.375L9.85417 7.5H5.5V17ZM5.5 17V7.5V9.5V17Z" fill="var(--colab-icon-color)" transform="scale(1.5) translate(-4 -4)"></path></svg></md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$--><svg viewBox="0 0 24 24"><!--?lit$019689205$-->
    <path d="M17.2292 13.6042L15.5833 10.7917C15.5278 10.6944 15.4583 10.625 15.375 10.5833C15.2917 10.5278 15.1944 10.5 15.0833 10.5H13.9167C13.8056 10.5 13.7083 10.5278 13.625 10.5833C13.5417 10.625 13.4722 10.6944 13.4167 10.7917L11.7708 13.6042C11.7153 13.7014 11.6875 13.7986 11.6875 13.8958C11.6875 13.9931 11.7153 14.0903 11.7708 14.1875L12.3542 15.2083C12.4097 15.3056 12.4792 15.3819 12.5625 15.4375C12.6597 15.4792 12.7639 15.5 12.875 15.5H16.1458C16.2569 15.5 16.3542 15.4792 16.4375 15.4375C16.5208 15.3819 16.5903 15.3056 16.6458 15.2083L17.25 14.1875C17.3056 14.0903 17.3264 13.9931 17.3125 13.8958C17.3125 13.7986 17.2847 13.7014 17.2292 13.6042ZM13.5625 13.8333L14.5 12.1667L15.4375 13.8333H13.5625ZM5.5 18.5C5.09722 18.5 4.74306 18.3542 4.4375 18.0625C4.14583 17.7569 4 17.4028 4 17V7.5C4 7.08333 4.14583 6.72917 4.4375 6.4375C4.74306 6.14583 5.09722 6 5.5 6H10.4792L12 7.5H18.5C18.9167 7.5 19.2708 7.64583 19.5625 7.9375C19.8542 8.22917 20 8.58333 20 9V17C20 17.4028 19.8542 17.7569 19.5625 18.0625C19.2708 18.3542 18.9167 18.5 18.5 18.5H5.5ZM5.5 17H18.5V9H11.375L9.85417 7.5H5.5V17ZM5.5 17V7.5V9.5V17Z" fill="var(--colab-icon-color)" transform="scale(1.5) translate(-4 -4)"></path>
    <line x1="2" y1="2" x2="22" y2="22" style="stroke:var(--colab-icon-color);stroke-width:2.5"></line></svg></md-icon>
          </md-icon-button>
          <md-icon-button toggle="" id="hidden-files-toggle" data-aria-label="Mostrar archivos ocultos" aria-label-selected="Ocultar archivos ocultos" title="Mostrar archivos ocultos" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar archivos ocultos" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility_off</md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility</md-icon>
          </md-icon-button>
        </div>
        <div class="parent-link"><div class="file-title-row">
          <!--?lit$019689205$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->folder</md-icon>
          <span class="file-tree-name" title="Subir un nivel">
            <!--?lit$019689205$-->..
          </span>
          <input class="file-tree-name-input" value="..">
          <!--?lit$019689205$--><md-icon-button class="file-item-action-button add-to-composer-button" id="add-to-composer-button-0" data-aria-label="Agregar a Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar a Gemini">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="add-to-composer-button-0" message="Agregar a Gemini"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar a Gemini</div><!----><!--?--></template>
    </colab-tooltip-trigger>
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Más acciones para el archivo: .." value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones para el archivo: .." aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div></div>
        <div class="files-root"><colab-file-view filename="content" draggable="true"><!----><!--?lit$019689205$--><!--?--><!--?lit$019689205$-->
        <div class="child-files"><colab-file-view filename="sample_data" class="collapsed" draggable="true"><!----><!--?lit$019689205$-->
        <div class="file-title-row">
          <!--?lit$019689205$--> <md-icon class="file-icon colab-icon directory-icon" style="margin-left: 0px;" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->folder</md-icon>
          <span class="file-tree-name" title="sample_data">
            <!--?lit$019689205$-->sample_data
          </span>
          <input class="file-tree-name-input" value="sample_data">
          <!--?lit$019689205$-->
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Más acciones para la carpeta: sample_data" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones para la carpeta: sample_data" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$019689205$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="El directorio es demasiado grande para mostrar todos los archivos." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view><colab-file-view filename="modelo-reg.pkl" draggable="true"><!----><!--?lit$019689205$-->
        <div class="file-title-row">
          <!--?lit$019689205$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->draft</md-icon>
          <span class="file-tree-name" title="modelo-reg.pkl (23.87K) 
Última modificación Sat Mar 28 2026 11:27:22 GMT-0500 (hora estándar de Colombia)">
            <!--?lit$019689205$-->modelo-reg.pkl
          </span>
          <input class="file-tree-name-input" value="modelo-reg.pkl">
          <!--?lit$019689205$--><md-icon-button class="file-item-action-button add-to-composer-button" id="add-to-composer-button-4" data-aria-label="Agregar a Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar a Gemini">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="add-to-composer-button-4" message="Agregar a Gemini"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar a Gemini</div><!----><!--?--></template>
    </colab-tooltip-trigger>
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Más acciones para el archivo: modelo-reg.pkl" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones para el archivo: modelo-reg.pkl" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$019689205$--><!--?--><!--?--></colab-file-view><colab-file-view filename="videojuegos-datosFuturos.csv" draggable="true"><!----><!--?lit$019689205$-->
        <div class="file-title-row">
          <!--?lit$019689205$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->csv</md-icon>
          <span class="file-tree-name" title="videojuegos-datosFuturos.csv (233) 
Última modificación Sat Mar 28 2026 11:26:41 GMT-0500 (hora estándar de Colombia)">
            <!--?lit$019689205$-->videojuegos-datosFuturos.csv
          </span>
          <input class="file-tree-name-input" value="videojuegos-datosFuturos.csv">
          <!--?lit$019689205$--><md-icon-button class="file-item-action-button add-to-composer-button" id="add-to-composer-button-3" data-aria-label="Agregar a Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar a Gemini">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="add-to-composer-button-3" message="Agregar a Gemini"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar a Gemini</div><!----><!--?--></template>
    </colab-tooltip-trigger>
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Más acciones para el archivo: videojuegos-datosFuturos.csv" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones para el archivo: videojuegos-datosFuturos.csv" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$019689205$--><!--?--><!--?--></colab-file-view></div>
        <div class="overflow-ellipsis" title="El directorio es demasiado grande para mostrar todos los archivos." style="margin-left: -20px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="files-drag-to-upload layout horizontal">
          <md-icon class="layout noshrink" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
          <div> <!--?lit$019689205$-->Arrastra archivos para subirlos al almacenamiento de sesión. </div>
        </div>
        <div class="files-uploading"></div>
        <div class="colab-usage-bar-container"><colab-usage-bar aria-describedby="file-browser-disk-display-kernel-tooltip" id="file-browser-disk-display-kernel" class="file-browser-disk-display usage-bar-with-suffix" tabindex="0" style="display: flex;"><template shadowrootmode="open"><!---->
        <div class="header">
          <div><!--?lit$019689205$-->Disco </div>
          <div class="suffix"><!--?lit$019689205$-->86.51 GB disponibles</div>
        </div>
        <!--?lit$019689205$-->
      <div class="progress-container">
        <md-linear-progress class="  " value="0.196855897200762"><template shadowrootmode="open"><!---->
      <div role="progressbar" aria-valuemin="0" class="progress   " aria-valuemax="1" aria-valuenow="0.196855897200762"><!--?lit$019689205$-->
      <div class="dots" hidden=""></div>
      <div class="inactive-track" style="transform: scaleX(1);"></div>
      <div class="bar primary-bar" style="transform: scaleX(0.196856);">
        <div class="bar-inner"></div>
      </div>
      <div class="bar secondary-bar">
        <div class="bar-inner"></div>
      </div>
    </div>
    </template></md-linear-progress>
      </div>
    
      </template></colab-usage-bar><colab-tooltip-trigger aria-hidden="true" id="file-browser-disk-display-kernel-tooltip"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Disco: 21.20 GB/107.72 GB</div><!----><!--?--></template></colab-tooltip-trigger></div></colab-file-tree></colab-file-browser></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$019689205$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$019689205$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-gG3ST0fuQfYc" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$019689205$--><div class="indicator"></div>
      </div>
      <!--?lit$019689205$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$019689205$--><div class="colab-tab-title">
      <!--?lit$019689205$-->
      <span id="tab-title-gG3ST0fuQfYc"><!--?lit$019689205$--><!--?lit$019689205$-->Cuaderno<!--?--></span>
    </div> <!--?lit$019689205$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$019689205$--><!--?--></div>
      <!--?lit$019689205$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="Más acciones de la pestaña" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones de la pestaña" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="Más acciones de la pestaña"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones de la pestaña</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button id="tab-pane-0-close-all-button" data-aria-label="Cerrar todas las pestañas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar todas las pestañas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-close-all-button" message="Cerrar todas las pestañas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar todas las pestañas</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-scroller role="main" id="notebook-main" class="notebook-container" aria-label="Cuaderno" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$019689205$-->
              <div class="notebook-content ">
                <!--?lit$019689205$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell" id="cell-r7c-OSGnQfYK" role="region" aria-label="Celda 0: Celda de código: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:25 a.m. (hace 0 minutos)
ejecutada en 0.52 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:25 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.52 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[1]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 86px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
   4
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Cargamos&nbsp;librerías&nbsp;principales</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;np</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;pd</span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;plt</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 0" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer role="group" tabindex="0"><div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-P7cflNqZRG62" role="region" aria-label="Celda 1: Celda de código: " style="opacity: 1;" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:27 a.m. (hace 17 minutos)
ejecutada en 1.503 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:27 a.m. (hace 17 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 1.503 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[2]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->1&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 181px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
   4
   5
   6
   7
   8
   9
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Cargamos&nbsp;el&nbsp;modelo</span></span><br><span><span></span></span><br><span><span class="mtk20">import</span><span class="mtk1">&nbsp;pickle</span></span><br><span><span></span></span><br><span><span class="mtk1">filename&nbsp;=&nbsp;</span><span class="mtk5">'modelo-reg.pkl'</span></span><br><span><span></span></span><br><span><span class="mtk1">modelo</span><span class="mtk14">,</span><span class="mtk1">&nbsp;min_max_scaler</span><span class="mtk14">,</span><span class="mtk1">&nbsp;variables&nbsp;=&nbsp;pickle.load</span><span class="mtk14">(</span><span class="mtk17">open</span><span class="mtk14">(</span><span class="mtk1">filename</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'rb'</span><span class="mtk14">))</span></span><br><span><span></span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 1" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-zBZ6wGXfRj7D" tabindex="-1" role="region" aria-label="Celda 2: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
Es posible que la celda se haya modificado desde que se ejecutó por última vez

ejecutada por Gloria Gil Ibarra
11:28 a.m. (hace 13 minutos)
ejecutada en 0.068 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->Es posible que la celda se haya modificado desde que se ejecutó por última vez</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:28 a.m. (hace 13 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.068 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[3]</div>
      <!--?lit$019689205$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 67px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Cargamos&nbsp;los&nbsp;datos&nbsp;futuros</span></span><br><span><span class="mtk8">#data&nbsp;=&nbsp;pd.read_csv("videojuegos-datosFuturos.csv"</span><span class="mtk8">)</span></span><br><span><span class="mtk8">#data.head()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 2" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 224px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe.html" class="" style="height: 224px;"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-Eo5eEAH3RoTJ" tabindex="-1" role="region" aria-label="Celda 3: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
Es posible que la celda se haya modificado desde que se ejecutó por última vez

ejecutada por Gloria Gil Ibarra
11:28 a.m. (hace 13 minutos)
ejecutada en 0.042 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->Es posible que la celda se haya modificado desde que se ejecutó por última vez</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:28 a.m. (hace 13 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.042 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[4]</div>
      <!--?lit$019689205$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="34" data-mode-id="notebook-python" style="height: 542px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; on, &quot;calt&quot; on;"><div class="monaco-editor no-user-select mac  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/7" style="width: 551px; height: 542px;"><div data-mprt="3" class="overflow-guard" style="width: 551px; height: 542px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 542px; width: 58px;"><div class="glyph-margin" style="left: 0px; width: 19px; height: 542px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute; width: 58px;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 58px; height: 542px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">3</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">4</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">5</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">6</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">7</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">8</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">9</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">10</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">11</div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">12</div></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">13</div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">14</div></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">15</div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="current-line" style="width:58px; height:19px;"></div><div class="line-numbers active-line-number" style="left:19px;width:17px;">16</div></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">17</div></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 58px; width: 493px; height: 542px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 542px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 493px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:59px;width:76px;height:19px;"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:74px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-right-radius" style="top:0px;left:74px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:92px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:92px;width:10px;height:19px;"></div><div class="cslr selected-text top-left-radius top-right-radius" style="top:0px;left:84px;width:8px;height:19px;"></div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="cslr selected-text top-left-radius bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:261px;height:19px;"></div><svg style="position:absolute;width:134px;height:19px" viewBox="0 0 134 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(227, 228, 226, 0.16)"><circle cx="46.21" cy="9.50" r="1.20"></circle><circle cx="63.21" cy="9.50" r="1.20"></circle><circle cx="130.21" cy="9.50" r="1.20"></circle></svg></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 542px; left: 674.375px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute; width: 776px;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 493px; height: 542px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Interfaz&nbsp;grafica</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk8">#Se&nbsp;crea&nbsp;interfaz&nbsp;gráfica&nbsp;con&nbsp;streamlit&nbsp;para&nbsp;</span><span class="mtk8">captura&nbsp;de&nbsp;</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk8">los&nbsp;datos</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Predicción&nbsp;de&nbsp;inversión&nbsp;en&nbsp;una&nbsp;tienda&nbsp;de&nbsp;</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk5">videojuegos'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">Edad&nbsp;=&nbsp;st.slider</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Edad'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;min_value=</span><span class="mtk6">14</span><span class="mtk14">,</span><span class="mtk1">&nbsp;max_value=</span><span class="mtk6">52</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">value=</span><span class="mtk6">20</span><span class="mtk14">,</span><span class="mtk1">&nbsp;step=</span><span class="mtk6">1</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">videojuego&nbsp;=&nbsp;st.selectbox</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Videojuego'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">"'Mass&nbsp;</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk5">Effect'"</span><span class="mtk14">,</span><span class="mtk5">"'Battlefield'"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"'Fifa'"</span><span class="mtk14">,</span><span class="mtk5">"'KOA:&nbsp;Reckoning'"</span><span class="mtk14">,</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk5">"'Crysis'"</span><span class="mtk14">,</span><span class="mtk5">"'Sim&nbsp;City'"</span><span class="mtk14">,</span><span class="mtk5">"'Dead&nbsp;Space'"</span><span class="mtk14">,</span><span class="mtk5">"'F1'"</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">Plataforma&nbsp;=&nbsp;st.selectbox</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Plataforma'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">"'Play&nbsp;</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk5">Station'"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"'Xbox'"</span><span class="mtk14">,</span><span class="mtk5">"PC"</span><span class="mtk14">,</span><span class="mtk5">"Otros"</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">Sexo&nbsp;=&nbsp;st.selectbox</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Sexo'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Hombre'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Mujer'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">Consumidor_habitual&nbsp;=&nbsp;st.selectbox</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Consumidor_habitual'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'True'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'False'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk8">#Dataframe</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">datos&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk1">Edad</span><span class="mtk14">,</span><span class="mtk1">&nbsp;videojuego</span><span class="mtk14">,</span><span class="mtk1">Plataforma</span><span class="mtk14">,</span><span class="mtk1">Sexo</span><span class="mtk14">,</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">Consumidor_habitual</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">data&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">datos</span><span class="mtk14">,</span><span class="mtk1">&nbsp;columns=</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Edad'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk5">'videojuego'</span><span class="mtk14">,</span><span class="mtk5">'Plataforma'</span><span class="mtk14">,</span><span class="mtk5">'Sexo'</span><span class="mtk14">,</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk5">'Consumidor_habitual'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;</span><span class="mtk8">#Dataframe&nbsp;con&nbsp;los&nbsp;mismos&nbsp;</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk8">nombres&nbsp;de&nbsp;variables</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (⌘.)" style="position: absolute; display: none; visibility: hidden; max-width: 776px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 418px; left: 260px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 479px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 479px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="28" height="1084" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 542px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 542px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 542px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 551px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 16.8594px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 418px; left: 58px; width: 472px; height: 19px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover margin"></div><div data-mprt="4" class="overlayWidgets" style="width: 551px;"><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesGlyphHoverWidget" style="position: absolute;"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 542px;"><div class="minimap-shadow-hidden" style="height: 542px;"></div><canvas width="0" height="1084" style="position: absolute; left: 0px; width: 0px; height: 542px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1084" style="position: absolute; left: 0px; width: 0px; height: 542px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash mac vertical" style="left: 8px;"></div><div class="monaco-sash mac vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north mac horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south mac horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 3" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-n2ypB_uSRq0V" tabindex="-1" role="region" aria-label="Celda 4: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
Es posible que la celda se haya modificado desde que se ejecutó por última vez

ejecutada por Gloria Gil Ibarra
11:29 a.m. (hace 0 minutos)
ejecutada en 0.037 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->Es posible que la celda se haya modificado desde que se ejecutó por última vez</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:29 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.037 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[5]</div>
      <!--?lit$019689205$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 143px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
   4
   5
   6
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Se&nbsp;realiza&nbsp;la&nbsp;preparación</span></span><br><span><span class="mtk1">data_preparada=data.copy</span><span class="mtk14">()</span></span><br><span><span class="mtk1">&nbsp;</span></span><br><span><span class="mtk8">#En&nbsp;despliegue&nbsp;drop_first=&nbsp;False,&nbsp;siempre&nbsp;va&nbsp;en&nbsp;fa</span><span class="mtk8">lse</span></span><br><span><span class="mtk1">data_preparada&nbsp;=&nbsp;pd.get_dummies</span><span class="mtk14">(</span><span class="mtk1">data_preparada</span><span class="mtk14">,</span><span class="mtk1">&nbsp;columns=</span><span class="mtk14">[</span><span class="mtk5">'videojuego'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Plataforma'</span><span class="mtk14">,</span><span class="mtk5">'Sexo'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Consumidor_habitual'</span><span class="mtk14">],</span><span class="mtk1">&nbsp;drop_first=</span><span class="mtk9">False</span><span class="mtk14">,</span><span class="mtk1">&nbsp;dtype=</span><span class="mtk16">int</span><span class="mtk14">)</span></span><br><span><span class="mtk1">data_preparada.head</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 4" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 244px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(1).html" class="" style="height: 244px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data_preparada</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-SNAtDb40SY3w" tabindex="-1" role="region" aria-label="Celda 5: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:31 a.m. (hace 0 minutos)
ejecutada en 0.062 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:31 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.062 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[6]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 67px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Se&nbsp;adicionan&nbsp;las&nbsp;columnas&nbsp;faltantes</span></span><br><span><span class="mtk1">data_preparada=data_preparada.reindex</span><span class="mtk14">(</span><span class="mtk1">columns=variables</span><span class="mtk14">,</span><span class="mtk1">fill_value=</span><span class="mtk6">0</span><span class="mtk14">)</span></span><br><span><span class="mtk1">data_preparada.head</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 5" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 244px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(2).html" class="" style="height: 244px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data_preparada</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-aOTbaPM9Sv8E" tabindex="-1" role="region" aria-label="Celda 6: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
Es posible que la celda se haya modificado desde que se ejecutó por última vez

ejecutada por Gloria Gil Ibarra
11:33 a.m. (hace 0 minutos)
ejecutada en 0.063 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->Es posible que la celda se haya modificado desde que se ejecutó por última vez</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:33 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.063 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[7]</div>
      <!--?lit$019689205$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 124px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
   4
   5
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Se&nbsp;normaliza&nbsp;la&nbsp;edad&nbsp;para&nbsp;predecir&nbsp;con&nbsp;Knn,&nbsp;Red,&nbsp;</span><span class="mtk8">SVM</span></span><br><span><span class="mtk8">#En&nbsp;los&nbsp;despliegues&nbsp;no&nbsp;se&nbsp;llama&nbsp;fit</span></span><br><span><span class="mtk8">#&nbsp;si&nbsp;alguien&nbsp;coge&nbsp;un&nbsp;arbol&nbsp;no&nbsp;se&nbsp;debe&nbsp;normalizar</span></span><br><span><span class="mtk1">data_preparada</span><span class="mtk14">[[</span><span class="mtk5">'Edad'</span><span class="mtk14">]]</span><span class="mtk1">=&nbsp;min_max_scaler.transform</span><span class="mtk14">(</span><span class="mtk1">data_preparada</span><span class="mtk14">[[</span><span class="mtk5">'Edad'</span><span class="mtk14">]])</span></span><br><span><span class="mtk1">data_preparada.head</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 6" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 244px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(3).html" class="" style="height: 244px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data_preparada</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell text notebook-cell" id="cell-4bcD6o0ETO61" tabindex="-1" role="region" aria-label="Celda 7: Celda de texto: Predicciones" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$019689205$--><!----><md-icon-button touch-target="none" id="markdown-toolbar-header-4bcD6o0ETO61" class="markdown-toolbar-header" aria-describedby="markdown-toolbar-header-4bcD6o0ETO61-tooltip" data-aria-label="Activar o desactivar encabezado" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activar o desactivar encabezado">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_size</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-header-4bcD6o0ETO61" id="markdown-toolbar-header-4bcD6o0ETO61-tooltip" message="Activar o desactivar encabezado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Activar o desactivar encabezado</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-bold-4bcD6o0ETO61" class="markdown-toolbar-bold" aria-describedby="markdown-toolbar-bold-4bcD6o0ETO61-tooltip" data-aria-label="Negrita" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Negrita">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_bold</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-bold-4bcD6o0ETO61" id="markdown-toolbar-bold-4bcD6o0ETO61-tooltip" message="Negrita"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Negrita</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-italic-4bcD6o0ETO61" class="markdown-toolbar-italic" aria-describedby="markdown-toolbar-italic-4bcD6o0ETO61-tooltip" data-aria-label="Aplicar cursiva" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Aplicar cursiva">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_italic</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-italic-4bcD6o0ETO61" id="markdown-toolbar-italic-4bcD6o0ETO61-tooltip" message="Aplicar cursiva"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Aplicar cursiva</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-code-4bcD6o0ETO61" class="markdown-toolbar-code" aria-describedby="markdown-toolbar-code-4bcD6o0ETO61-tooltip" data-aria-label="Aplicar formato como código" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Aplicar formato como código">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->code</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-code-4bcD6o0ETO61" id="markdown-toolbar-code-4bcD6o0ETO61-tooltip" message="Aplicar formato como código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Aplicar formato como código</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-link-4bcD6o0ETO61" class="markdown-toolbar-link" aria-describedby="markdown-toolbar-link-4bcD6o0ETO61-tooltip" data-aria-label="Insertar vínculo" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insertar vínculo">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->link</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-link-4bcD6o0ETO61" id="markdown-toolbar-link-4bcD6o0ETO61-tooltip" message="Insertar vínculo"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar vínculo</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><label for="markdown-image-input-4bcD6o0ETO61" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-4bcD6o0ETO61" aria-describedby="markdown-toolbar-insert-image-4bcD6o0ETO61-tooltip" aria-label="Insertar imagen">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-insert-image-4bcD6o0ETO61" id="markdown-toolbar-insert-image-4bcD6o0ETO61-tooltip" message="Insertar imagen"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar imagen</div><!----><!--?--></template></colab-tooltip-trigger>
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-4bcD6o0ETO61"><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-blockquote-4bcD6o0ETO61" class="markdown-toolbar-blockquote" aria-describedby="markdown-toolbar-blockquote-4bcD6o0ETO61-tooltip" data-aria-label="Agregar bloque entrecomillado" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar bloque entrecomillado">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_quote</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-blockquote-4bcD6o0ETO61" id="markdown-toolbar-blockquote-4bcD6o0ETO61-tooltip" message="Agregar bloque entrecomillado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar bloque entrecomillado</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-ol-4bcD6o0ETO61" class="markdown-toolbar-ol" aria-describedby="markdown-toolbar-ol-4bcD6o0ETO61-tooltip" data-aria-label="Agregar lista numerada" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar lista numerada">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_list_numbered</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-ol-4bcD6o0ETO61" id="markdown-toolbar-ol-4bcD6o0ETO61-tooltip" message="Agregar lista numerada"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar lista numerada</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-ul-4bcD6o0ETO61" class="markdown-toolbar-ul" aria-describedby="markdown-toolbar-ul-4bcD6o0ETO61-tooltip" data-aria-label="Agregar lista con viñetas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar lista con viñetas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-ul-4bcD6o0ETO61" id="markdown-toolbar-ul-4bcD6o0ETO61-tooltip" message="Agregar lista con viñetas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar lista con viñetas</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-hr-4bcD6o0ETO61" class="markdown-toolbar-hr" aria-describedby="markdown-toolbar-hr-4bcD6o0ETO61-tooltip" data-aria-label="Agregar regla horizontal" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar regla horizontal">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->horizontal_rule</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-hr-4bcD6o0ETO61" id="markdown-toolbar-hr-4bcD6o0ETO61-tooltip" message="Agregar regla horizontal"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar regla horizontal</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-latex-4bcD6o0ETO61" class="markdown-toolbar-latex" aria-describedby="markdown-toolbar-latex-4bcD6o0ETO61-tooltip" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-latex-4bcD6o0ETO61" id="markdown-toolbar-latex-4bcD6o0ETO61-tooltip" message="LaTeX"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->LaTeX</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-emoji-4bcD6o0ETO61" class="markdown-toolbar-emoji" aria-describedby="markdown-toolbar-emoji-4bcD6o0ETO61-tooltip" data-aria-label="Insertar emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insertar emoji">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->mood</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-emoji-4bcD6o0ETO61" id="markdown-toolbar-emoji-4bcD6o0ETO61-tooltip" message="Insertar emoji"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar emoji</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-preview-4bcD6o0ETO61" class="markdown-toolbar-preview" aria-describedby="markdown-toolbar-preview-4bcD6o0ETO61-tooltip" data-aria-label="Reubicar la vista previa de Markdown" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reubicar la vista previa de Markdown">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$--><svg viewBox="0 0 24 24"><!--?lit$019689205$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-preview-4bcD6o0ETO61" id="markdown-toolbar-preview-4bcD6o0ETO61-tooltip" message="Reubicar la vista previa de Markdown"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Reubicar la vista previa de Markdown</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-text-button id="markdown-toolbar-close-editor-4bcD6o0ETO61" class="markdown-toolbar-close-editor" aria-describedby="markdown-toolbar-close-editor-4bcD6o0ETO61-tooltip" data-aria-label="Cerrar el editor Markdown" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Cerrar el editor Markdown">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <!--?lit$019689205$-->Cerrar
        </md-text-button>
        <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-close-editor-4bcD6o0ETO61" id="markdown-toolbar-close-editor-4bcD6o0ETO61-tooltip" message="Cerrar el editor Markdown"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar el editor Markdown</div><!----><!--?--></template></colab-tooltip-trigger><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="25" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; on, &quot;calt&quot; on; display: none;"><div class="monaco-editor no-user-select mac  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/11" style="width: 441px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 441px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 435px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 435px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:435px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 435px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">#&nbsp;Predicciones</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (⌘.)" style="position: absolute; display: none; visibility: hidden; max-width: 435px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 117px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 421px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 421px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="28" height="58" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 441px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 16.8594px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 413px; height: 19px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 441px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="58" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="58" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash mac vertical" style="left: 8px;"></div><div class="monaco-sash mac vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north mac horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south mac horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Contraer 2 celdas secundarias en Predicciones (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)" data-aria-label="Contraer 2 celdas secundarias en Predicciones (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Contraer 2 celdas secundarias en Predicciones (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Predicciones</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--> <!--?lit$019689205$-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="Haz clic para expandir">
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>subdirectory_arrow_right</md-icon>
          <span>2 celdas ocultas</span>
        </div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-2R4PmsXBTShf" tabindex="-1" role="region" aria-label="Celda 8: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:37 a.m. (hace 0 minutos)
ejecutada en 0.007 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:37 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.007 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[8]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 67px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
   3
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#Hacemos&nbsp;la&nbsp;predicción&nbsp;con&nbsp;el&nbsp;Tree</span></span><br><span><span class="mtk1">Y_pred&nbsp;=&nbsp;modelo.predict</span><span class="mtk14">(</span><span class="mtk1">data_preparada</span><span class="mtk14">)</span></span><br><span><span class="mtk17">print</span><span class="mtk14">(</span><span class="mtk1">Y_pred</span><span class="mtk14">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 8" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>[ 20. 100. 200. 300. 600.]
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-wNwmCOH9T039" tabindex="-1" role="region" aria-label="Celda 9: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:38 a.m. (hace 0 minutos)
ejecutada en 0.061 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:38 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.061 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[9]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 48px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">data</span><span class="mtk14">[</span><span class="mtk5">'Prediccion'</span><span class="mtk14">]</span><span class="mtk1">=Y_pred</span></span><br><span><span class="mtk1">data.head</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 9" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 244px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(4).html" class="" style="height: 244px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell text notebook-cell" id="cell-mQmUpfWIT414" tabindex="-1" role="region" aria-label="Celda 10: Celda de texto: Data" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$019689205$--><!----><md-icon-button touch-target="none" id="markdown-toolbar-header-mQmUpfWIT414" class="markdown-toolbar-header" aria-describedby="markdown-toolbar-header-mQmUpfWIT414-tooltip" data-aria-label="Activar o desactivar encabezado" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activar o desactivar encabezado">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_size</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-header-mQmUpfWIT414" id="markdown-toolbar-header-mQmUpfWIT414-tooltip" message="Activar o desactivar encabezado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Activar o desactivar encabezado</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-bold-mQmUpfWIT414" class="markdown-toolbar-bold" aria-describedby="markdown-toolbar-bold-mQmUpfWIT414-tooltip" data-aria-label="Negrita" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Negrita">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_bold</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-bold-mQmUpfWIT414" id="markdown-toolbar-bold-mQmUpfWIT414-tooltip" message="Negrita"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Negrita</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-italic-mQmUpfWIT414" class="markdown-toolbar-italic" aria-describedby="markdown-toolbar-italic-mQmUpfWIT414-tooltip" data-aria-label="Aplicar cursiva" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Aplicar cursiva">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_italic</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-italic-mQmUpfWIT414" id="markdown-toolbar-italic-mQmUpfWIT414-tooltip" message="Aplicar cursiva"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Aplicar cursiva</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-code-mQmUpfWIT414" class="markdown-toolbar-code" aria-describedby="markdown-toolbar-code-mQmUpfWIT414-tooltip" data-aria-label="Aplicar formato como código" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Aplicar formato como código">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->code</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-code-mQmUpfWIT414" id="markdown-toolbar-code-mQmUpfWIT414-tooltip" message="Aplicar formato como código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Aplicar formato como código</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-link-mQmUpfWIT414" class="markdown-toolbar-link" aria-describedby="markdown-toolbar-link-mQmUpfWIT414-tooltip" data-aria-label="Insertar vínculo" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insertar vínculo">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->link</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-link-mQmUpfWIT414" id="markdown-toolbar-link-mQmUpfWIT414-tooltip" message="Insertar vínculo"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar vínculo</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><label for="markdown-image-input-mQmUpfWIT414" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-mQmUpfWIT414" aria-describedby="markdown-toolbar-insert-image-mQmUpfWIT414-tooltip" aria-label="Insertar imagen">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-insert-image-mQmUpfWIT414" id="markdown-toolbar-insert-image-mQmUpfWIT414-tooltip" message="Insertar imagen"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar imagen</div><!----><!--?--></template></colab-tooltip-trigger>
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-mQmUpfWIT414"><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-blockquote-mQmUpfWIT414" class="markdown-toolbar-blockquote" aria-describedby="markdown-toolbar-blockquote-mQmUpfWIT414-tooltip" data-aria-label="Agregar bloque entrecomillado" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar bloque entrecomillado">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_quote</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-blockquote-mQmUpfWIT414" id="markdown-toolbar-blockquote-mQmUpfWIT414-tooltip" message="Agregar bloque entrecomillado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar bloque entrecomillado</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-ol-mQmUpfWIT414" class="markdown-toolbar-ol" aria-describedby="markdown-toolbar-ol-mQmUpfWIT414-tooltip" data-aria-label="Agregar lista numerada" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar lista numerada">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_list_numbered</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-ol-mQmUpfWIT414" id="markdown-toolbar-ol-mQmUpfWIT414-tooltip" message="Agregar lista numerada"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar lista numerada</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-ul-mQmUpfWIT414" class="markdown-toolbar-ul" aria-describedby="markdown-toolbar-ul-mQmUpfWIT414-tooltip" data-aria-label="Agregar lista con viñetas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar lista con viñetas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-ul-mQmUpfWIT414" id="markdown-toolbar-ul-mQmUpfWIT414-tooltip" message="Agregar lista con viñetas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar lista con viñetas</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-hr-mQmUpfWIT414" class="markdown-toolbar-hr" aria-describedby="markdown-toolbar-hr-mQmUpfWIT414-tooltip" data-aria-label="Agregar regla horizontal" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar regla horizontal">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->horizontal_rule</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-hr-mQmUpfWIT414" id="markdown-toolbar-hr-mQmUpfWIT414-tooltip" message="Agregar regla horizontal"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar regla horizontal</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-latex-mQmUpfWIT414" class="markdown-toolbar-latex" aria-describedby="markdown-toolbar-latex-mQmUpfWIT414-tooltip" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-latex-mQmUpfWIT414" id="markdown-toolbar-latex-mQmUpfWIT414-tooltip" message="LaTeX"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->LaTeX</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-emoji-mQmUpfWIT414" class="markdown-toolbar-emoji" aria-describedby="markdown-toolbar-emoji-mQmUpfWIT414-tooltip" data-aria-label="Insertar emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insertar emoji">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->mood</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-emoji-mQmUpfWIT414" id="markdown-toolbar-emoji-mQmUpfWIT414-tooltip" message="Insertar emoji"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Insertar emoji</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-icon-button touch-target="none" id="markdown-toolbar-preview-mQmUpfWIT414" class="markdown-toolbar-preview" aria-describedby="markdown-toolbar-preview-mQmUpfWIT414-tooltip" data-aria-label="Reubicar la vista previa de Markdown" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reubicar la vista previa de Markdown">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$--><svg viewBox="0 0 24 24"><!--?lit$019689205$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-preview-mQmUpfWIT414" id="markdown-toolbar-preview-mQmUpfWIT414-tooltip" message="Reubicar la vista previa de Markdown"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Reubicar la vista previa de Markdown</div><!----><!--?--></template></colab-tooltip-trigger><!----><!----><md-text-button id="markdown-toolbar-close-editor-mQmUpfWIT414" class="markdown-toolbar-close-editor" aria-describedby="markdown-toolbar-close-editor-mQmUpfWIT414-tooltip" data-aria-label="Cerrar el editor Markdown" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Cerrar el editor Markdown">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <!--?lit$019689205$-->Cerrar
        </md-text-button>
        <colab-tooltip-trigger aria-hidden="true" for="markdown-toolbar-close-editor-mQmUpfWIT414" id="markdown-toolbar-close-editor-mQmUpfWIT414-tooltip" message="Cerrar el editor Markdown"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar el editor Markdown</div><!----><!--?--></template></colab-tooltip-trigger><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="28" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; on, &quot;calt&quot; on; display: none;"><div class="monaco-editor no-user-select mac  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/14" style="width: 441px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 441px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 435px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 435px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:435px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 435px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">#&nbsp;Data</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (⌘.)" style="position: absolute; display: none; visibility: hidden; max-width: 435px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 50px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 421px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 421px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="28" height="58" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 441px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 16.8594px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 413px; height: 19px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 441px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="58" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="58" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash mac vertical" style="left: 8px;"></div><div class="monaco-sash mac vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north mac horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south mac horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Contraer 2 celdas secundarias en Data (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)" data-aria-label="Contraer 2 celdas secundarias en Data (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)" style="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Contraer 2 celdas secundarias en Data (Presiona &lt;Mayúsculas&gt; para contraer también las secciones del mismo nivel)">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Data</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--> <!--?lit$019689205$-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="Haz clic para expandir">
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>subdirectory_arrow_right</md-icon>
          <span>2 celdas ocultas</span>
        </div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-wFGohIECT-L-" tabindex="-1" role="region" aria-label="Celda 11: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación

ejecutada por Gloria Gil Ibarra
11:40 a.m. (hace 0 minutos)
ejecutada en 0.037 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:40 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.037 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[10]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->check</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style="height: 48px; overflow: hidden;"><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">   1
   2
</pre><pre class="monaco-colorized colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Predicciones&nbsp;finales</span></span><br><span><span class="mtk1">data</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$019689205$-->Comienza a programar o <span tabindex="0" role="button" class="link">generar</span> con IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 11" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 244px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(5).html" class="" style="height: 244px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Generar código con <code>data</code>
          </md-outlined-button><!----><!----><md-outlined-button class="interactive-sheet" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            New interactive sheet
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Agregar celda de código
⌘/Ctrl+M B" title="Agregar celda de código
⌘/Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de código
⌘/Ctrl+M B">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Código
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Agregar celda de texto" title="Agregar celda de texto" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-label="Agregar celda de texto">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$019689205$-->Texto
        </md-outlined-button>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell focused code-has-output" id="cell-fCL7wnn1WE2K" tabindex="-1" role="region" aria-label="Celda 12: Celda de código: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$019689205$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Mover celda hacia arriba
⌘/Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mover celda hacia arriba
⌘/Ctrl+M K">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->arrow_upward</md-icon>
        <!--?lit$019689205$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Mover celda hacia arriba
⌘/Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mover celda hacia arriba</div><!----><!----><div><!--?lit$019689205$-->⌘/Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Mover celda hacia abajo
⌘/Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value="" soft-disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mover celda hacia abajo
⌘/Ctrl+M J" aria-disabled="true">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->arrow_downward</md-icon>
        <!--?lit$019689205$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Mover celda hacia abajo
⌘/Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mover celda hacia abajo</div><!----><!----><div><!--?lit$019689205$-->⌘/Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$019689205$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-fCL7wnn1WE2K" anchor="ai-menu-anchor-fCL7wnn1WE2K" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$019689205$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$019689205$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Generar código</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Explicar el código</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$019689205$-->Transforma el código</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-fCL7wnn1WE2K-tooltip" data-aria-label="Funciones basadas en IA disponibles" id="ai-menu-anchor-fCL7wnn1WE2K" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Funciones basadas en IA disponibles" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template> pen_spark </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-fCL7wnn1WE2K" id="ai-menu-anchor-fCL7wnn1WE2K-tooltip" message="Funciones basadas en IA disponibles"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Funciones basadas en IA disponibles</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Editar" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Editar" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->edit</md-icon>
        <!--?lit$019689205$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Editar"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Editar</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Borrar celda
⌘/Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Borrar celda
⌘/Ctrl+M D">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->delete</md-icon>
        <!--?lit$019689205$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Borrar celda
⌘/Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Borrar celda</div><!----><!----><div><!--?lit$019689205$-->⌘/Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="Más acciones en la celda" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones en la celda" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="Más acciones en la celda"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones en la celda</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused error">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Ejecutar celda" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$019689205$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$019689205$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$019689205$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Ejecutar celda (⌘/Ctrl+Enter)
La celda se ejecutó desde la última modificación
No se pudo realizar la ejecución anterior de la celda

ejecutada por Gloria Gil Ibarra
11:48 a.m. (hace 0 minutos)
ejecutada en 0.048 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Ejecutar celda (⌘/Ctrl+Enter)</div><!----><!----><div><!--?lit$019689205$-->La celda se ejecutó desde la última modificación</div><!----><!----><div><!--?lit$019689205$-->No se pudo realizar la ejecución anterior de la celda</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->ejecutada por Gloria Gil Ibarra</div><!----><!----><div><!--?lit$019689205$-->11:48 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.048 segundos</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$019689205$--><div class="status">
      <div class="execution-count"><!--?lit$019689205$-->[11]</div>
      <!--?lit$019689205$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->error</md-icon>
      <div><!--?lit$019689205$-->0&nbsp;s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="48" data-mode-id="notebook-python" style="height: 67px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; on, &quot;calt&quot; on;"><div class="monaco-editor no-user-select mac  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/16" style="width: 551px; height: 67px;"><div data-mprt="3" class="overflow-guard" style="width: 551px; height: 67px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 67px; width: 58px;"><div class="glyph-margin" style="left: 0px; width: 19px; height: 67px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 58px; height: 67px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:19px;width:17px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:58px; height:19px;"></div><div class="line-numbers active-line-number" style="left:19px;width:17px;">3</div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 58px; width: 493px; height: 67px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 67px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 493px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="current-line" style="width:493px; height:19px;"></div><div class="cdr wordHighlightText" style="left:25px;width:59px;height:19px;"></div><div class="cdr squiggly-error" style="left:0px;width:379px;height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 493px; height: 67px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Recordar&nbsp;medida&nbsp;de&nbsp;error&nbsp;del&nbsp;modelo</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">st.warning</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"El&nbsp;modelo&nbsp;tiene&nbsp;un&nbsp;error&nbsp;del&nbsp;9%"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (⌘.)" style="position: absolute; display: none; visibility: hidden; max-width: 493px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 38px; left: 75px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 479px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 479px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="28" height="134" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 67px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 67px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 67px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 551px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 16.8594px; font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 38px; left: 58px; width: 472px; height: 19px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover margin"></div><div data-mprt="4" class="overlayWidgets" style="width: 551px;"><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesGlyphHoverWidget" style="position: absolute;"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 67px;"><div class="minimap-shadow-hidden" style="height: 67px;"></div><canvas width="0" height="134" style="position: absolute; left: 0px; width: 0px; height: 67px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="134" style="position: absolute; left: 0px; width: 0px; height: 67px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 52px; width: 305px; z-index: 50; display: none; visibility: hidden; max-width: 1470px; top: 380.688px; left: 533px;"><div class="monaco-sash mac vertical" style="left: 303px;"></div><div class="monaco-sash mac vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north mac horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south mac horizontal disabled" style="top: 50px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 305px; height: 52px;"><div class="monaco-scrollable-element  mac" role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px; width: 305px; height: 52px;"><div class="hover-row"><div class="marker hover-contents" style="font-family: monospace, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot;, &quot;calt&quot;; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><span style="white-space: pre-wrap;">NameError: name 'st' is not defined</span></div></div><div class="hover-row status-bar"><div class="actions"><div class="action-container" tabindex="0"><a class="action" role="button"><span>View Problem (⌥F8)</span></a></div><div>No quick fixes available</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 295px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 295px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 52px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 52px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Resultado de la celda 12" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$019689205$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Mostrar/ocultar resultado" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mostrar/ocultar resultado" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Mostrar/ocultar resultado"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mostrar/ocultar resultado</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button focused" data-aria-label="Acciones para el resultado de las celdas de código" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Acciones para el resultado de las celdas de código" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Acciones para el resultado de las celdas de código"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Acciones para el resultado de las celdas de código</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 216px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(6).html" class="" style="height: 216px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
      <span class="next-steps-title"> <!--?lit$019689205$-->Próximos pasos: </span>
      <!--?lit$019689205$--><!----><md-outlined-button class="fix" data-test-id="explain-error" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
            <!--?lit$019689205$-->Explicar error
          </md-outlined-button><!---->
    </div></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comentarios" style="display: none;"></section></div>
          <!--?lit$019689205$--> <div class="footer-links" style="padding-bottom: 8px;">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$019689205$-->Productos pagados de Colab
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$019689205$-->Cancela los contratos aquí
      </a>
    </div>
        </div>
      </colab-scroller>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$019689205$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$019689205$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="Más acciones de la pestaña" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones de la pestaña" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="Más acciones de la pestaña"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones de la pestaña</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button id="tab-pane-2-close-all-button" data-aria-label="Cerrar todas las pestañas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar todas las pestañas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-close-all-button" message="Cerrar todas las pestañas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar todas las pestañas</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize"><div class="resizer-thumb"></div>
        <!--?lit$019689205$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$019689205$--><colab-tab-pane class="layout vertical grow" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" aria-labelledby="tab-title--hWqXm5HQfaD" draggable="true" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$019689205$--><div class="indicator"></div>
      </div>
      <!--?lit$019689205$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$019689205$--><div class="colab-tab-title">
      <!--?lit$019689205$-->
      <span id="tab-title--hWqXm5HQfaD"><!--?lit$019689205$--><!--?lit$019689205$-->Gemini<!--?--></span>
    </div> <!--?lit$019689205$--><md-icon-button class="tab-close" data-aria-label="Cerrar" title="Cerrar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon></md-icon-button> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$019689205$--><!----><md-icon-button class="tab-action" data-aria-label="Mover al cuaderno" title="Mover al cuaderno" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mover al cuaderno">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->collapse_content</md-icon>
        </md-icon-button><!----><!--?--></div>
      <!--?lit$019689205$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="Más acciones de la pestaña" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones de la pestaña" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="Más acciones de la pestaña"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones de la pestaña</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button id="tab-pane-1-close-all-button" data-aria-label="Cerrar todas las pestañas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar todas las pestañas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-close-all-button" message="Cerrar todas las pestañas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar todas las pestañas</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow selected-tab"><colab-composer view-mode="tab" style="transform: translate(0px, 0px);"><template shadowrootmode="open"><!---->
      <colab-composer-conversation><template shadowrootmode="open"><!---->
      <div class="scrollable">
        <!--?lit$019689205$--><colab-composer-zero-state><template shadowrootmode="open"><!---->
      <section class="container">
        <h2 class="greeting"><!--?lit$019689205$-->Hola Gloria</h2>
        <span class="sub-greeting"><!--?lit$019689205$-->¿En qué puedo ayudarte?</span>
        <!--?lit$019689205$-->
      <colab-composer-suggestion-chips tab-zero-state=""><template shadowrootmode="open"><!---->
      <div class=" suggestion-chips tab-mode tab-zero-state ">
        <!--?lit$019689205$--><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$-->
        <span class="suggestion-text"><!--?lit$019689205$-->¿Cómo hago para instalar bibliotecas de Python?</span>
      </md-outlined-button>
    <!----><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$-->
        <span class="suggestion-text"><!--?lit$019689205$-->Carga datos de Google Drive</span>
      </md-outlined-button>
    <!----><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <!--?lit$019689205$-->
        <span class="suggestion-text"><!--?lit$019689205$-->Muestra un ejemplo de entrenamiento de un modelo de AA simple</span>
      </md-outlined-button>
    <!---->
      </div>
    </template></colab-composer-suggestion-chips>
    
      </section>
    </template></colab-composer-zero-state>
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
      </div>
    </template>
      </colab-composer-conversation>
      <!--?lit$019689205$-->
      <div class="footer">
        <!--?lit$019689205$--> <!--?lit$019689205$-->
        <div class="input-container">
          <colab-composer-input><template shadowrootmode="open"><!---->
      <div class="wrapper">
        <!--?lit$019689205$-->
        <!--?lit$019689205$-->
              <div class="text-field-wrapper"> <!--?lit$019689205$--><colab-composer-rich-text-field class="composer-input-field"><template shadowrootmode="open"><!---->
      <div class="colab-monaco-wrapper">
        <!--?lit$019689205$--><div class="colab-monaco-placeholder">
              <!--?lit$019689205$-->¿Qué puedo ayudarte a crear?
            </div>
        <div class="colab-monaco-container" data-keybinding-context="2" data-mode-id="plaintext" style="height: 20px; --vscode-editorCodeLens-lineHeight: 17px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #282a2c; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #282a2c;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #282a2c;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #282a2c;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #282a2c;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #282a2c;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #282a2c; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><div class="monaco-editor no-user-select mac  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/4" style="width: 286px; height: 24px;"><div data-mprt="3" class="overflow-guard" style="width: 286px; height: 24px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 24px; width: 0px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 24px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: &quot;Google Sans Text&quot;, Roboto, sans-serif, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 20px; letter-spacing: 0px; width: 0px; height: 24px;"><div style="position:absolute;top:0px;width:100%;height:20px;"><div class="current-line" style="width:0px; height:20px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark mac" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 0px; width: 286px; height: 24px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: &quot;Google Sans Text&quot;, Roboto, sans-serif, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 20px; letter-spacing: 0px; height: 0px; width: 286px;"><div style="position:absolute;top:0px;width:100%;height:20px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: &quot;Google Sans Text&quot;, Roboto, sans-serif, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 20px; letter-spacing: 0px; width: 286px; height: 24px;"><div style="top:0px;height:20px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 20px; top: 0px; left: 0px; font-family: &quot;Google Sans Text&quot;, Roboto, sans-serif, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 20px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 276px; height: 0px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 276px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="0" height="0" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 10px; height: 24px; display: none;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 24px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 24px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 286px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 14.3438px; font-family: &quot;Google Sans Text&quot;, Roboto, sans-serif, Menlo, Monaco, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 20px; letter-spacing: 0px; top: 0px; left: 0px; width: 268px; height: 20px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 286px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 24px;"><div class="minimap-shadow-hidden" style="height: 24px;"></div><canvas width="0" height="48" style="position: absolute; left: 0px; width: 0px; height: 24px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="48" style="position: absolute; left: 0px; width: 0px; height: 24px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"></div></div></div>
        <div class="autocomplete-anchor"></div>
        <colab-composer-autocomplete class="autocomplete-menu"><template shadowrootmode="open"><!----><md-menu id="menu" aria-controls="menu" aria-autocomplete="list" aria-expanded="true" aria-activedescendant="1" positioning="popover" role="listbox" anchor-corner="end-end" default-focus="none" aria-label="Elementos que se autocompletaron" menu-corner="end-start" y-offset="10" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$019689205$--><slot></slot> </div>
        </div>
      </div>
    </template>
      <!--?lit$019689205$-->
    </md-menu></template>
        </colab-composer-autocomplete>
      </div>
    </template>
        </colab-composer-rich-text-field> </div>
              <div class="actions">
                <div class="left-side-actions">
                  <!--?lit$019689205$-->
      <md-icon-button data-aria-haspopup="true" id="add-context" data-aria-label="Agregar a Gemini" data-aria-expanded="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Agregar a Gemini" aria-haspopup="true" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="add-context" message="Agregar a Gemini"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Agregar a Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-menu positioning="popover" quick="" aria-labelledby="add-context" anchor="add-context" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$019689205$--><slot></slot> </div>
        </div>
      </div>
    </template>
        <!--?lit$019689205$-->
      <md-menu-item md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>folder</md-icon>
        <span slot="headline"><!--?lit$019689205$-->Seleccionar archivos</span>
      </md-menu-item>
      <md-menu-item md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload</md-icon>
        <span slot="headline"><!--?lit$019689205$-->Subir</span>
      </md-menu-item>
    
        <!--?lit$019689205$-->
      </md-menu>
    
                  <!--?lit$019689205$-->
                  <!--?lit$019689205$-->
                </div>
                <div class="right-side-actions">
                  <colab-composer-model-selector><template shadowrootmode="open"><!---->
      <md-filled-select data-aria-haspopup="true" data-aria-label="Selecciona el modelo de Gemini" class="model-select" value="gemini-2.5-flash" display-text="Gemini 2.5 Flash"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="select   ">
        <!--?lit$019689205$-->
      <md-filled-field aria-haspopup="listbox" role="combobox" part="field" id="field" aria-describedby="description" aria-controls="listbox" class="field" has-end="" aria-label="Selecciona el modelo de Gemini" aria-expanded="false" label="" supporting-text="" error-text="" tabindex="0"><template shadowrootmode="open"><!---->
      <div class="field  with-end populated no-label ">
        <div class="container-overflow">
          <!--?lit$019689205$--> <div class="background"></div> 
          <slot name="container"></slot>
          <!--?lit$019689205$--> <div class="state-layer"></div>  <!--?lit$019689205$--><div class="active-indicator"></div> <!--?lit$019689205$-->
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$019689205$--> <!--?lit$019689205$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$019689205$-->
      </div>
    </template>
         <!--?lit$019689205$--><!---->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    <!----><!----><div id="label"><!--?lit$019689205$-->Gemini 2.5 Flash</div><!----><!---->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon">
          <svg height="5" viewBox="7 10 10 5" focusable="false">
            <polygon class="down" stroke="none" fill-rule="evenodd" points="7 10 12 15 17 10"></polygon>
            <polygon class="up" stroke="none" fill-rule="evenodd" points="7 15 12 10 17 15"></polygon>
          </svg>
        </slot>
      </span>
    <!---->
         <div id="description" slot="aria-describedby"></div>
      </md-filled-field> <!--?lit$019689205$--><div class="menu-wrapper">
      <md-menu id="listbox" role="listbox" stay-open-on-focusout="" part="menu" exportparts="focus-ring: menu-focus-ring" anchor="field" no-navigation-wrap="" aria-label="Selecciona el modelo de Gemini" style="--__menu-min-width: 0px;" aria-hidden="true" tabindex="-1"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$019689205$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$019689205$--><slot></slot> </div>
        </div>
      </div>
    </template>
        <!--?lit$019689205$--><slot></slot>
      </md-menu>
    </div>
      </span>
    </template>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--> <!--?lit$019689205$--><!---->
      <md-select-option value="gemini-2.5-flash" display-text="Gemini 2.5 Flash" md-menu-item="" data-aria-selected="true" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="option" class="list-item selected" aria-selected="true" tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <!--?lit$019689205$--><div slot="headline">
      <div class="model-name"><!--?lit$019689205$-->Gemini 2.5 Flash</div>
      <!--?lit$019689205$--><div class="model-subtitle"><!--?lit$019689205$-->Ayuda veloz y versátil</div>
    </div>
      </md-select-option>
    <!----><!---->
      <md-select-option value="gemini-3.0-flash" display-text="Gemini 3 Flash" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="option" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <!--?lit$019689205$--><div slot="headline">
      <div class="model-name"><!--?lit$019689205$-->Gemini 3 Flash</div>
      <!--?lit$019689205$--><div class="model-subtitle"><!--?lit$019689205$-->Inteligencia de vanguardia diseñada para la velocidad</div>
    </div>
      </md-select-option>
    <!----> <!--?lit$019689205$--><md-select-option class="upsell-option" value="gemini_3_upgrade" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="option" class="list-item   " tabindex="0"><!--?lit$019689205$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$019689205$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$019689205$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$019689205$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
      <div class="model-with-button" slot="headline">
        <div>
          <div class="model-name"><!--?lit$019689205$-->Gemini 3 Pro</div>
          <div class="model-subtitle">
            <!--?lit$019689205$-->Para suscriptores de Pro
          </div>
        </div>
        <md-outlined-button class="upsell-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <!--?lit$019689205$-->Actualizar
        </md-outlined-button>
      </div>
    </md-select-option> 
      </md-filled-select>
    </template>
                  </colab-composer-model-selector>
                  <!--?lit$019689205$--><md-icon-button id="send" data-aria-label="Enviar" aria-describedby="send-tooltip" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Enviar" aria-disabled="true">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>send</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="send" id="send-tooltip" message="Enviar"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Enviar</div><!----><!--?--></template>
      </colab-tooltip-trigger>
                </div>
              </div>
            
      </div>
      <!--?lit$019689205$-->
      <input type="file" hidden="" multiple="">
    </template></colab-composer-input>
          <!--?lit$019689205$-->
      <div class="floating-actions-wrapper">
        <div class="floating-actions-hideable-container">
          <!--?lit$019689205$--><!--?lit$019689205$-->
      <md-icon-button touch-target="none" id="move-to-side-panel" data-aria-label="Mover al panel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mover al panel">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_content</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="move-to-side-panel" message="Mover al panel"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Mover al panel</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    <!--?lit$019689205$--><md-icon-button touch-target="none" id="close" data-aria-label="Cerrar" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="close" message="Cerrar"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?-->
        </div>
      </div>
    
        </div>
        <!--?lit$019689205$--> <!--?lit$019689205$-->
      </div>
      <!--?lit$019689205$-->
    
    </template></colab-composer></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$019689205$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$019689205$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="Más acciones de la pestaña" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Más acciones de la pestaña" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="Más acciones de la pestaña"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Más acciones de la pestaña</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$019689205$--><md-icon-button id="tab-pane-3-close-all-button" data-aria-label="Cerrar todas las pestañas" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cerrar todas las pestañas">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-close-all-button" message="Cerrar todas las pestañas"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Cerrar todas las pestañas</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./app.ipynb_files/outputframe(7).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./app.ipynb_files/outputframe(8).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowrootmode="open"><!---->
      <md-icon-button toggle="" id="toggle-composer-button" data-aria-label="Activar o desactivar Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activar o desactivar Gemini" aria-pressed="false">
        <!--?lit$019689205$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$019689205$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$019689205$--><span class="icon"><slot></slot></span>
        <!--?lit$019689205$-->
        <!--?lit$019689205$--><span class="touch"></span>
  </button></template>
        <!--?lit$019689205$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer-button" message="Activar o desactivar Gemini"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Activar o desactivar Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-status-bar role="region" aria-label="Barra de estado del entorno de ejecución"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="right">
        <!--?lit$019689205$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template><!--?lit$019689205$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>error</md-icon><!--?lit$019689205$-->11:48 a.m.</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Enfocar la última celda ejecutada

11:48 a.m. (hace 0 minutos)
ejecutada en 0.008 segundos"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Enfocar la última celda ejecutada</div><!----><!----><br><!----><!----><div><!--?lit$019689205$-->11:48 a.m. (hace 0 minutos)</div><!----><!----><div><!--?lit$019689205$-->ejecutada en 0.008 segundos</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$019689205$--><!--?lit$019689205$--><!--?lit$019689205$--><colab-runtime-status><template shadowrootmode="open"><!----><md-text-button data-aria-expanded="false" data-aria-haspopup="menu" id="runtime-options" aria-describedby="runtime-options-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button" aria-haspopup="menu" aria-expanded="false">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dns</md-icon><!--?lit$019689205$-->Python 3</md-text-button><colab-tooltip-trigger aria-hidden="true" for="runtime-options" id="runtime-options-tooltip" message="Opciones del entorno de ejecución"><template shadowrootmode="open"><!----><!--?lit$019689205$--><!----><div><!--?lit$019689205$-->Opciones del entorno de ejecución</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->data_object</md-icon>
        <!--?lit$019689205$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$019689205$-->terminal</md-icon>
        <!--?lit$019689205$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 643px; visibility: visible; left: 70px; top: 62px;" aria-activedescendant=":b"><!--?lit$019689205$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ubicar en Drive<!--?lit$019689205$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Abrir en modo de sitio de pruebas<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Nuevo notebook en Drive<!--?lit$019689205$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Abrir bloc de notas<!--?lit$019689205$--><span class="goog-menuitem-accel">⌘/Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Subir notebook<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Renombrar<!--?lit$019689205$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mover<!--?lit$019689205$--></div></div><div command="trash" class="goog-menuitem goog-menuitem-highlight" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mover a la papelera<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar una copia en Drive<!--?lit$019689205$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar una copia como Gist en GitHub<!--?lit$019689205$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar una copia en GitHub<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar<!--?lit$019689205$--><span class="goog-menuitem-accel">⌘/Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar y fijar revisión<!--?lit$019689205$--><span class="goog-menuitem-accel">⌘/Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Historial de revisión<!--?lit$019689205$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Información del bloc de notas<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$019689205$-->Descargar
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Imprimir<!--?lit$019689205$--><span class="goog-menuitem-accel">⌘/Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Descargar .ipynb<!--?lit$019689205$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Descargar .py<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Deshacer<!--?lit$019689205$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Rehacer<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":t" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Seleccionar todas las celdas<!--?lit$019689205$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Cortar celda o selección<!--?lit$019689205$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Copiar celda o selección<!--?lit$019689205$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Pegar<!--?lit$019689205$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Borrar las celdas seleccionadas<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":z" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Buscar y reemplazar<!--?lit$019689205$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Buscar siguiente<!--?lit$019689205$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":12" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Buscar anterior<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":13" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":14" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Configuración del notebook<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":15" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":16" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Borrar todos los resultados<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$019689205$-->Índice<!--?lit$019689205$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Historial de códigos ejecutados<!--?lit$019689205$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Iniciar presentación de diapositivas<!--?lit$019689205$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Iniciar presentación de diapositivas desde el principio<!--?lit$019689205$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$019689205$-->Comentarios
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ocultar secciones<!--?lit$019689205$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Expandir secciones<!--?lit$019689205$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Guardar el diseño de la sección contraída<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mostrar/ocultar código<!--?lit$019689205$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mostrar/ocultar resultado<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Enfocar pestaña siguiente<!--?lit$019689205$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Enfocar pestaña anterior<!--?lit$019689205$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mover la pestaña al panel siguiente<!--?lit$019689205$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Mover la pestaña al panel anterior<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ocultar comentarios<!--?lit$019689205$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Minimizar comentarios<!--?lit$019689205$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Expandir comentarios<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Celda de código<!--?lit$019689205$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Celda de texto<!--?lit$019689205$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Celda de encabezado de la sección<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Celda de código temporal<!--?lit$019689205$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Fragmentos de código<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Agregar un campo de formulario<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ejecutar todo<!--?lit$019689205$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ejecutar celdas anteriores a la seleccionada<!--?lit$019689205$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ejecutar la celda enfocada<!--?lit$019689205$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ejecutar selección<!--?lit$019689205$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ejecutar celda y elementos secundarios<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Interrumpir la ejecución<!--?lit$019689205$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Reiniciar la sesión<!--?lit$019689205$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Reiniciar la sesión y ejecutar todas las celdas<!--?lit$019689205$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Desconectar y borrar el tiempo de ejecución<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Cambiar tipo de entorno de ejecución<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Administrar sesiones<!--?lit$019689205$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ver recursos<!--?lit$019689205$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ver registros del entorno de ejecución<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="deploy-cloud-run" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Implementar en Google Cloud Run<!--?lit$019689205$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Paleta de comandos<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2m" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Configuración<!--?lit$019689205$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Combinaciones de teclas<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2p" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Diferencias entre cuadernos<!--?lit$019689205$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$019689205$-->(se abre en una pestaña nueva)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$019689205$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Preguntas frecuentes<!--?lit$019689205$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ver notas de la versión<!--?lit$019689205$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Buscar fragmentos de código<!--?lit$019689205$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2v" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Informar sobre un error<!--?lit$019689205$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Denunciar abuso en Drive<!--?lit$019689205$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Enviar comentarios<!--?lit$019689205$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ver las Condiciones del Servicio<!--?lit$019689205$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":30" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$019689205$-->Ver en inglés<!--?lit$019689205$--></div></div></div><dialog class="doc-comments-area" aria-label="Comentarios"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$019689205$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$019689205$--><button id="button" class="button">
      <!--?lit$019689205$-->
      <span class="touch"></span>
      <!--?lit$019689205$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$019689205$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$019689205$-->Agregar un comentario
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">from tkinter import *
from tkinter import ttk
from tkinter import messagebox</div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy0d36475035724b5fbf2810b397f43388795b25f80.3339559352" name="apiproxy0d36475035724b5fbf2810b397f43388795b25f80.3339559352" src="./app.ipynb_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-z9n5adxm6d74" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./app.ipynb_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./app.ipynb_files/saved_resource.html"></iframe></div><iframe src="./app.ipynb_files/bscframe.html" style="display: none;"></iframe></body><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integration></html>