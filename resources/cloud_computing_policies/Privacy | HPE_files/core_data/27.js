(window.webpackJsonp=window.webpackJsonp||[]).push([[27],{"3y+j":function(e,t,n){},"BA/U":function(e,t,n){"use strict";n.d(t,"a",function(){return c});var c=function onKeyDownSubmit(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];return function(n){(function isEnter(e){return"Enter"===e.key||13===e.keyCode}(n)||t&&function isSpace(e){return"Space"===e.key||32===e.keyCode}(n))&&(n.preventDefault(),e())}}},BY8A:function(e,t,n){"use strict";var c=n("s8DI"),a=n("QtlZ"),o=n("Hvhg"),i=n("ERkP"),r=n.n(i),s=n("rTkt");n("zoZM");t.a=function ThemeStyleSheets(){var e=Object(i.useState)(!1),t=Object(c.a)(e,2),n=t[0],u=t[1],l=Object(o.b)(Object(a.b)());return Object(i.useEffect)(function(){n||(Object(s.a)(l),Object(s.b)(l),u(!0))},[l,n]),r.a.createElement("div",{className:"drift-widget-preload-fonts","aria-hidden":"true"},r.a.createElement("span",null,"A"),r.a.createElement("strong",null,"B"))}},NJR1:function(e,t,n){},"ab+K":function(e,t,n){"use strict";var c=n("/UYI"),a=n("nQD+"),o=n("Za8o"),i=n("LwEI"),r=n("ERkP"),s=n.n(r);n("NJR1");t.a=function MessageCloseButton(e){var t=e.onClick,n=e.shouldFocus,u=void 0!==n&&n,l=Object(i.a)(),d=Object(r.useRef)(null);Object(o.a)(d,u);return s.a.createElement(a.a,{onClick:function handleOnClick(e){(null===d||void 0===d?void 0:d.current)&&(null===d||void 0===d||d.current.blur()),t(e)},ref:d,className:"drift-widget-message-close-button drift-widget-close-button--align-".concat(l),"aria-label":"Close Drift Widget messenger preview overlay"},s.a.createElement(c.a,{width:10,height:10}))}},dT9Q:function(e,t,n){"use strict";var c=n("s8DI"),a=n("BA/U"),o=n("ab+K"),i=n("7oh4"),r=n("nedb"),s=n("Erxq"),u=n("58kB"),l=n("hEj5"),d=n("IJKc"),f=n("LwEI"),b=n("SsZN"),O=n("vjCh"),j=n("qixE"),g=n("xwTo"),v=n("da4L"),h=n("X9/c"),m=n("g6eD"),p=n("2XY6"),E=n("i9gz"),w=n("RhEL"),C=n("LVcX"),k=n("ERkP"),S=n.n(k),I=n("uDfI"),R=n("vTYT"),_=n("y0on");n("pUpc");t.a=function MessagePreview(){var e=Object(l.a)(),t=Object(c.a)(e,2),n=t[0],y=t[1],D=Object(I.b)(),N=Object(k.useState)(null),A=Object(c.a)(N,2),M=A[0],L=A[1],T=Object(I.c)(function(e){return e.conversations}).activeConversation,J=Object(I.c)(function(e){return e.session.gdpr}),P=Object(d.a)(),x=Object(r.a)(),B=Object(I.c)(p.f),U=Object(I.c)(function(e){return e.view.chatOpen}),W=Object(f.a)(),H=Object(u.a)(M?M.authorId:null).recipient,Z=Object(k.useMemo)(function(){return!(J.dismissedConsent||!M||!M.body||U)},[M,U,J.dismissedConsent]);Object(k.useEffect)(function setLatestMessageFromConvo(){if(Object(E.a)(P))L(null);else{var e=P.pop()||{};M&&Object(w.a)(e.id,M.id)||L(Object(v.s)(e,100))}},[P]),Object(k.useLayoutEffect)(function updateFrameSize(){if(Z){var e=n?n.width:0,t=n?n.height:0,c=e+i.b+40,a=t+36;Object(h.c)(a,c)}},[n,Z]);var K=Object(s.a)(M);if(!Z)return null;var F=function dismiss(){M&&(Object(j.c)(T),L({}),Object(h.b)(),X())},X=function dismissPlaybookIfNotInteracted(){if(!Object(g.i)()){var e=Object(C.a)(null,["attributes","playbookId"],x);Object(b.o)(M),Object(O.l)(x.id,e)}},z=function openChat(){if(Object(h.b)(),K){var e=Object(C.a)(null,["attributes","playbookId"],x);Object(b.n)(M),Object(O.l)(x.id,e)}D(Object(m.e)({chatOpen:!0}))},G=Object(v.b)(M),Q=Object(_.a)(H.name,G);return B?S.a.createElement("div",{className:"drift-widget-message-preview-wrapper",key:"".concat(M.id,"-preview-box")},S.a.createElement("div",{className:"drift-widget-message-preview drift-widget-message-preview--align-".concat(W)},W===R.a.RIGHT&&S.a.createElement(o.a,{onClick:F}),S.a.createElement("div",{onClick:z,onKeyDown:Object(a.a)(z),className:"drift-widget-message-preview-text drift-widget-message-preview-text--align-".concat(W),"aria-label":"".concat(Q?Q+" - ":"","Open chat"),"aria-live":"polite",tabIndex:0,role:"button"},S.a.createElement("span",{ref:y},G)),W===R.a.LEFT&&S.a.createElement(o.a,{onClick:F}))):null}},g3yi:function(e,t,n){"use strict";var c=n("nfbA"),a=n("efbE"),o=n("LeJ0"),i=function getDefaultAuthParams(e){return{embed_id:e,client_id:o.a.CLIENT_ID,consent_id:"has_consent"}};n.d(t,"b",function(){return r}),n.d(t,"a",function(){return s});var r=function executeWidgetBootstrapForMode(e,t){switch(e){case"LANDING_PAGE":return l(t);case"CHAT":default:return u(t)}},s=function executeBootstrapPing(e){return a.c.post("widget_bootstrap/ping",e)},u=function widgetBootstrap(e){var t=i(e.embed_id);return a.b.post("widget_bootstrap",{data:Object(c.a)(Object(c.a)({},t),e)})},l=function landingPageBootstrap(e){var t=i(e.embed_id);return a.b.post("widget_bootstrap/landing_page",{data:Object(c.a)(Object(c.a)({},t),e)})}},pUpc:function(e,t,n){},xKh3:function(e,t,n){"use strict";n.d(t,"b",function(){return h}),n.d(t,"a",function(){return m});var c=n("mj2O"),a=n.n(c),o=n("7SM1"),i=n("uIJS"),r=n("wQh9"),s=n("LeJ0"),u=n("QtlZ"),l=n("xwTo"),d=n("qwiD"),f=n("P2Ru"),b=n("ADGC"),O=n("0lfv"),j=n("l+Xe"),g=n("/l56"),v=new(function(){function RefetchMessagesState(){Object(i.a)(this,RefetchMessagesState),this.isJoinAfterConnectionLost=void 0,this.isJoinAfterConnectionLost=!1}return Object(r.a)(RefetchMessagesState,[{key:"shouldRefetchMessagesOnChannelJoin",value:function shouldRefetchMessagesOnChannelJoin(){return this.isJoinAfterConnectionLost}},{key:"onSocketDisconnect",value:function onSocketDisconnect(){this.isJoinAfterConnectionLost=!0}},{key:"resetStateOnJoin",value:function resetStateOnJoin(){this.isJoinAfterConnectionLost=!1}}]),RefetchMessagesState}()),h=function OpenSocket(e){var t=e.session_token,n=e.org_id,c=e.socketCluster,a=e.ip,o=s.a.WS_PROTOCOL,i="LOCAL"===s.a.WS_USER_ENV?"":"".concat(n,"-"),r=p(n,i,c),u="".concat(o,"://").concat(r,"/ws"),l=new f.a(u,{params:{session_token:t,remote_ip:a},timeout:1e4,reconnectAfterMs:function reconnectAfterMs(e){return[1e3,2e3,5e3,1e4][e-1]||1e4},rejoinAfterMs:function rejoinAfterMs(e){return[1e3,2e3,5e3][e-1]||1e4}});return l.connect(),l.onError(function(){c===g.c.CHAT&&(Object(O.n)({data:["ERROR - chat cluster disconnected on org: ".concat(n,", on IP: ").concat(a)],internal:!0}),v.onSocketDisconnect())}),l.onClose(function(){c===g.c.CHAT&&(Object(O.n)({data:["CLOSE - chat cluster disconnected on org: ".concat(n,", on IP: ").concat(a)],internal:!0}),v.onSocketDisconnect())}),l},m=function(){var e=Object(o.a)(a.a.mark(function _callee2(e){var t,n,c,i;return a.a.wrap(function _callee2$(r){for(;;)switch(r.prev=r.next){case 0:return t=e.channelName,n=e.socket,c=e.events,i=new Promise(function(){var e=Object(o.a)(a.a.mark(function _callee(e,o){var i;return a.a.wrap(function _callee$(a){for(;;)switch(a.prev=a.next){case 0:i=n.channel(t),c.forEach(function(e){var t=e.topic,n=e.event;i.on(t,n)}),i.join().receive("ok",function(){Object(l.i)()&&v.shouldRefetchMessagesOnChannelJoin()&&t.startsWith(g.b.USER)&&(Object(O.n)({data:["joined user channel ".concat(t," after disconnect and user interacted with active conversation"),"is_mobile_".concat(Object(b.c)(!0))],internal:!0}),u.a.dispatch(Object(d.w)({channel:g.b.USER,shouldRefetchMessagesForActiveConversation:!0})),v.resetStateOnJoin()),e({channel:i})}).receive("error",function(e){Object(O.n)({data:["Error connecting to channel: ".concat(t)]}),o(e)}).receive("timeout",function(e){Object(O.n)({data:["Joining the ".concat(t," channel timed out. ")]})});case 3:case"end":return a.stop()}},_callee)}));return function(t,n){return e.apply(this,arguments)}}()),r.abrupt("return",i);case 3:case"end":return r.stop()}},_callee2)}));return function JoinChannel(t){return e.apply(this,arguments)}}(),p=function _resolveSocketBaseForType(e,t,n){switch(n){case g.c.CHAT:return"".concat(Object(j.d)(e));case g.c.USER:return s.a.WS_USER_BASE;case g.c.PRESENCE:return"".concat(t).concat(Object(j.c)(e));case g.c.VISITOR_PRESENCE:return s.a.WS_VISITOR_PRESENCE_BASE;default:return""}}},yXOZ:function(e,t,n){"use strict";var c=n("s8DI"),a=n("BA/U"),o=n("O94r"),i=n.n(o),r=n("+Kbs"),s=n("yEsl"),u=n("hSLT"),l=n("nedb"),d=n("mZ4K"),f=n("UvQv"),b=n("fL0f"),O=n("Za8o"),j=n("Erxq"),g=n("tLIi"),v=n("hhdZ"),h=n("58kB"),m=n("lE29"),p=n("cwuI"),E=n("IJKc"),w=n("LwEI"),C=n("Hnjx"),k=n("SsZN"),S=n("vjCh"),I=n("g6eD"),R=n("2XY6"),_=n("LVcX"),y=n("i9gz"),D=n("0B8E"),N=n("ERkP"),A=n.n(N),M=n("Tr4L"),L=n("uDfI"),T=n("ADGC"),J=n("MFhO"),P=n("7oto"),x=n("1kux"),B=(n("3y+j"),"SENDER"),U="MEGAPHONE",W="THEME_ICON";t.a=function WidgetIcon(){var e=Object(N.useState)(!1),t=Object(c.a)(e,2),n=t[0],o=t[1],H=Object(N.useRef)(null);Object(O.a)(H,n);var Z=Object(f.a)(),K=Z.isDisabled,F=Z.setIsDisabled,X=Object(L.b)(),z=Object(M.a)().t,G=Object(L.c)(function(e){return e.view.chatOpen}),Q=Object(L.c)(function(e){return e.session.gdpr}),V=Object(L.c)(R.f),Y=Object(L.c)(function(e){return!!e.conversations.activeConversation}),q=Object(w.a)(),$=Object(l.a)(),ee=Object(L.c)(function(e){return Object(_.a)(!1,["embed","configuration","theme"],e)}).unreadBadgeEnabled,te=Object(E.a)(),ne=Object(L.c)(function(e){return e.view.isChatTakeover}),ce=Object(L.c)(function(e){return e.conversations}).activeConversation,ae=Object(v.a)(ce),oe=Object(g.a)(),ie=Object(y.a)(oe)?ae:oe,re=Object(j.a)(ie),se=Object(m.a)(),ue=se.backgroundStyles,le=se.widgetSecondaryColor,de=Object(p.a)(),fe=de.Icon,be=de.customIcon,Oe=de.hasCustomIcon,je=Object(d.a)(),ge=Object(u.a)().type,ve=je||Object(_.a)(void 0,["authorId"],ie),he=Object(h.a)(ve).recipient,me=te?Object(D.a)(te).length:0,pe=ge===J.a.SLIDER,Ee=ve&&(pe||me>0),we=Object(b.a)(["titleNotificationEnabled"]),Ce=Object(c.a)(we,1)[0],ke=void 0!==Ce&&Ce,Se=Object(N.useMemo)(function(){return Ee?B:pe&&!ve?U:W},[ve,pe,Ee]),Ie=Object(C.a)();Object(N.useEffect)(function(){ke&&Object(P.a)({topic:"page-notification-update",message:{totalUnreadMessages:me,pageTitleNotificationMsg:z("titleNotifier.newMessageNotification")}})},[me,ke,z]),Object(N.useEffect)(function(){K&&!pe&&F(!1)},[K,pe,F]),Object(N.useEffect)(function(){Object(P.a)({topic:"toggle-widget-controller",message:{isChatTakeover:ne,open:G,hasActiveConversation:Y&&Q.hasConsent}})},[G,Q,Y,ne]),Object(N.useEffect)(function(){te&&te.length>0&&Object(x.a)()},[te]),Object(N.useEffect)(function(){Object(P.c)({topic:"CONDUCTOR:focusWidgetIcon",handler:function handler(){return o(!0)}})},[]);var Re=function onToggleChat(){if(!G&&me>0&&re){var e=Object(_.a)(null,["attributes","playbookId"],$);Object(S.l)($.id,e),Object(k.n)(ie),Object(k.p)(ie)}!function toggle(e){if(pe)Object(P.a)({topic:"slider:showDetails",message:{}}),F(!0);else{var t=!Q.hasConsent&&!Q.declinedConsent;X(Object(I.e)({chatOpen:e,gdprDismissed:t}))}e&&Object(P.a)({topic:"reset-controller-size"})}(!G)},_e=Object(N.useMemo)(function(){return!Oe||Ee||G?null:be},[be,Ee,G,Oe]),ye=Object(N.useMemo)(function(){if(G)return he.name!==z("agent")?"Close chat with ".concat(he.name," in the Drift Widget messenger"):"Close Drift Widget messenger";var e=he.name!==z("agent")?"Open chat with ".concat(he.name," in the Drift Widget messenger"):"Open Drift Widget messenger";return ee&&me>0?"".concat(e," - Unread messages: ").concat(me):e},[G,he.name,z,ee,me]);if(!V)return null;var De={"--bgColor":ue.background,"--bgColorHover":ue.backgroundOnHover};return A.a.createElement("div",{className:i()("drift-widget-controller drift-widget-controller--align-".concat(q),[Ie],{"drift-widget-controller--closed":!Object(T.c)()&&G,"drift-widget-controller--custom-icon":Oe,"drift-widget-controller--avatar":Ee,"drift-widget-controller--hide":ne,"drift-widget-controller--disabled":K}),onClick:Re,style:De,"aria-label":ye,"aria-disabled":K,"aria-hidden":K,role:"button",tabIndex:K?-1:0,onKeyDown:Object(a.a)(Re),ref:H},A.a.createElement("div",{className:i()("drift-widget-controller-icon",[Ie],{"drift-widget-controller-icon--default":Oe&&!Ee&&!G}),style:_e},A.a.createElement("div",{className:"drift-controller-icon--active"},Se===U&&A.a.createElement(r.n,{fill:le}),Se===B&&A.a.createElement(s.a,{className:i()([Ie],"drift-controller-icon--avatar"),avatarClassName:i()([Ie],"drift-controller-icon--avatar-avatar"),id:ve}),Se===W&&!Oe&&fe),A.a.createElement("div",{className:"drift-controller-icon--close",style:{backgroundColor:le}})),ee&&me>0&&A.a.createElement("div",{className:"drift-controller-icon-unread"},Math.min(me,99)))}},zoZM:function(e,t,n){}}]);