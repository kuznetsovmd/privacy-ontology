/*|1.93.2.95-S-95|publish|2022-06-14T14:48:16.765Z|*/
!function(n){n.version=n.version||"1.93.2.95-S-95",n.time=n.time||new Date(1655218096765)}(window["~hpe~"]||(window["~hpe~"]={})),(window["~hpeWpJsonp~"]=window["~hpeWpJsonp~"]||[]).push([[116],{"hpe-my-account/modal-signinup-initializer":function(n,i,t){"use strict";Object.defineProperty(i,"__esModule",{value:!0}),i.initialize=void 0;var a=t("core/helpers/component"),l=t("core/helpers/config");i.initialize=function(i){var e,o;(0,l.getConfig)("myAccount.modalSignIn")&&!document.querySelector(".modal-signinup-overlay")&&(e=i,(o=document.createElement("div")).className="modal-signinup-overlay modal",o.setAttribute("tabIndex","-1"),o.setAttribute("role","dialog"),o.setAttribute("aria-labelledby","HPEModalSignIn"),document.body.appendChild(o),a.initComponent.$if(e(o))&&Promise.all([t.e(0),t.e(1),t.e(6),t.e(117)]).then(function(n){a.initComponent.$if(e(o))&&(0,a.initComponent)(t("hpe-my-account/modal-signinup-overlay"),e(o))}.bind(null,t)).catch(function(n){t("core/log").error("Can't load hpe-my-account/modal-signinup-overlay",n)})),a.initComponent.$if(i(".js-modal-signinup-trigger"))&&t.e(118).then(function(n){a.initComponent.$if(i(".js-modal-signinup-trigger"))&&(0,a.initComponent)(t("hpe-my-account/modal-signinup-trigger"),i(".js-modal-signinup-trigger"))}.bind(null,t)).catch(function(n){t("core/log").error("Can't load hpe-my-account/modal-signinup-trigger",n)})}}}]);