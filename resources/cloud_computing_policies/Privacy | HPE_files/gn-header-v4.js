/*|1.93.2.95-S-95|publish|2022-06-14T14:48:16.765Z|*/
!function(t){t.version=t.version||"1.93.2.95-S-95",t.time=t.time||new Date(1655218096765)}(window["~hpe~"]||(window["~hpe~"]={})),(window["~hpeWpJsonp~"]=window["~hpeWpJsonp~"]||[]).push([[108],{"core/helpers/metrics-my-account":function(t,e,o){"use strict";o.r(e),o.d(e,"MetricsMyAccount",function(){return a});function n(t){return t.replace(".html","").split("/").slice(3).join(":")||""}var r=o("core/helpers/metrics"),e=o(24),i=o.n(e),c=function(){return(c=Object.assign||function(t){for(var e,o=1,n=arguments.length;o<n;o++)for(var r in e=arguments[o])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t}).apply(this,arguments)},a=(s.trackCreateAccountStart=function(t){void 0===t&&(t=s.getParentPageForCreateAccount),Object(r.trackMetrics)(s.hvaCreateAccountStart,{parentPage:t()})},s.trackCreateAccountComplete=function(t,e){void 0===t&&(t=s.getParentPageForCreateAccount),Object(r.trackMetrics)(s.hvaCreateAccountComplete,{parentPage:t(),emid:e})},s.trackSignInSuccess=function(t,e,o){void 0===o&&(o=!1),s.islockedSignInSuccessMutex()||(Object(r.trackMetrics)(s.hvaSignInSuccess,{parentPage:s.getParentPageForSignInSuccess(e,o),emid:t}),s.lockSignInSuccessMutex())},s.trackSignInFailure=function(){Object(r.trackMetrics)(s.hvaSignInFailure,{parentPage:s.getParentPageFromCurrent()})},s.fireLoginStartEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:c({page_name:"login:modal"},t&&{emid:t})}))},s.fireLoginSuccessEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"login:modal:success",emid:t}}))},s.fireLoginFailEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"login:modal:fail",emid:t}}))},s.fireCreateAccountStartEvent=function(){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"create-account:modal:start"}}))},s.fireCreateAccountCompleteEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"create-account:modal:complete",emid:t}}))},s.islockedSignInSuccessMutex=function(){return"1"===i.a.get(s.hvaSignInSuccess)},s.lockSignInSuccessMutex=function(){i.a.set(s.hvaSignInSuccess,"1")},s.unlockSignInSuccessMutex=function(){i.a.set(s.hvaSignInSuccess,"0")},s.getParentPageFromCurrent=function(){return n(window.location.pathname)},s.getParentPageFromReferer=function(){return n(new URL(document.referrer).pathname)},s.getParentPageForCreateAccount=function(){if(document.referrer){var t=new URLSearchParams(window.location.search);if(t.has("redirectURL"))return t.get("redirectURL");if(!t.has("resource")&&Object(r.isReferrerMatch)())return s.getParentPageFromReferer()}return"no-parent-page"},s.getParentPageForSignInSuccess=function(t,e){if(t.includes("passport")){t="no-parent-page";return e?t=s.getParentPageFromCurrent():document.referrer&&(t=Object(r.isReferrerMatch)()?s.getParentPageFromReferer():s.getParentPageFromCurrent()),t}return s.getParentPageFromCurrent()},s.hvaCreateAccountStart="hva.createaccount.start",s.hvaCreateAccountComplete="hva.createaccount.complete",s.hvaSignInSuccess="hva.sign-in.success",s.hvaSignInFailure="hva.sign-in.failure",s.eventMetrics="ANALYTICS.PAGEVIEW",s);function s(){}},"hpe-gn/flyout-primary/gn-flyout-primary-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return h});var n,r,i=o(1),c=o("hpe-gn/flyout/gn-flyout-v4"),a=o(4),s=o(2),l=o(0),u=o(119),p=o(33),f=o("core/helpers/dom"),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},y=function(t,e){var o="function"==typeof Symbol&&t[Symbol.iterator];if(!o)return t;var n,r,i=o.call(t),c=[];try{for(;(void 0===e||0<e--)&&!(n=i.next()).done;)c.push(n.value)}catch(t){r={error:t}}finally{try{n&&!n.done&&(o=i.return)&&o.call(i)}finally{if(r)throw r.error}}return c},d=function(t,e,o){if(o||2===arguments.length)for(var n,r=0,i=e.length;r<i;r++)!n&&r in e||((n=n||Array.prototype.slice.call(e,0,r))[r]=e[r]);return t.concat(n||Array.prototype.slice.call(e))},h=(r=c.a,e(b,r),Object.defineProperty(b.prototype,"$gnHeaderMobile",{get:function(){return document.querySelector("gn-header-mobile")},enumerable:!1,configurable:!0}),Object.defineProperty(b.prototype,"$search",{get:function(){return document.querySelector("gn-header-search")},enumerable:!1,configurable:!0}),Object.defineProperty(b.prototype,"$backBtn",{get:function(){return this.querySelector(".gn-mobile-back-btn")},enumerable:!1,configurable:!0}),Object.defineProperty(b.prototype,"$calloutContent",{get:function(){return Array.from(this.querySelectorAll(".gn-callout-content"))},enumerable:!1,configurable:!0}),b.prototype.connectedCallback=function(){r.prototype.connectedCallback.call(this),this.classList.add(c.a.is),this._onDebouncedAlign()},b.prototype.bindEvents=function(){r.prototype.bindEvents.call(this),this.$search.addEventListener("esl:hide",this._onSearchHide),this.$search.addEventListener("keyup",this._onKeyboardEvent),this.$backBtn.addEventListener("click",this._onBackBtnClick),window.addEventListener("resize",this._onDebouncedAlign),window.addEventListener("fonts:loaded",this._onDebouncedAlign,{once:!0})},b.prototype.onShow=function(t){r.prototype.onShow.call(this,t),this.$gnHeaderMobile.hide({initiator:"flyout-primary",activator:this})},b.prototype.unbindEvents=function(){r.prototype.unbindEvents.call(this),this.$search.removeEventListener("esl:hide",this._onSearchHide),this.$search.removeEventListener("keyup",this._onKeyboardEvent),this.$backBtn.removeEventListener("click",this._onBackBtnClick),window.removeEventListener("resize",this._onDebouncedAlign),window.removeEventListener("fonts:loaded",this._onDebouncedAlign)},b.prototype._onSearchHide=function(){this.hide({initiator:"search-hide",activator:this})},b.prototype._onKeyboardEvent=function(t){if(this.open&&t.key===a.TAB){var e=this.$boundaryFocusable;return p.a.for("@-MD").matches?Object(u.b)(t,this.$search.$input,e.last)||Object(u.b)(t,e.first,this.$search.$closeBtn):Object(u.b)(t,e.first,e.last)}return r.prototype._onKeyboardEvent.call(this,t)},b.prototype._onOutsideAction=function(t){p.a.for("@-MD").matches||r.prototype._onOutsideAction.call(this,t)},b.prototype._onBackBtnClick=function(){this.hide({initiator:"back-btn",activator:this}),this.$gnHeaderMobile.show({initiator:"flyout-primary",activator:this})},b.prototype._onAlign=function(){var t,e;p.a.for("@-MD").matches?this.$calloutContent.forEach(function(t){return t.style.removeProperty("height")}):(t=this.$calloutContent.map(function(t){return t.scrollHeight}),e=Math.max.apply(Math,d([],y(t),!1)),this.$calloutContent.forEach(function(t){return t.style.height="".concat(e,"px")}))},b.is="gn-flyout-primary",o([Object(i.a)({defaultValue:"gn-flyout-opened gn-primary-flyout-opened"})],b.prototype,"bodyClass",void 0),o([Object(s.a)()],b.prototype,"$gnHeaderMobile",null),o([Object(s.a)()],b.prototype,"$search",null),o([Object(s.a)()],b.prototype,"$backBtn",null),o([Object(s.a)()],b.prototype,"$calloutContent",null),o([l.a],b.prototype,"_onSearchHide",null),o([l.a],b.prototype,"_onKeyboardEvent",null),o([l.a],b.prototype,"_onOutsideAction",null),o([l.a],b.prototype,"_onBackBtnClick",null),o([l.a],b.prototype,"_onAlign",null),b);function b(){var t=null!==r&&r.apply(this,arguments)||this;return t._onDebouncedAlign=Object(f.rafDecorator)(t._onAlign),t}},"hpe-gn/flyout/gn-flyout-logout-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return f});var n,r,i=o(0),c=o(21),a=o("hpe-gn/primary/gn-user-profile-v4"),s=o("core/log"),l=o("core/helpers/aem"),u=o("core/helpers/metrics-my-account"),p=o("cockpit/api/shared"),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},f=(r=c.a,e(y,r),y.prototype.connectedCallback=function(){this.$logoutTrigger=this.querySelector(".js-logout-trigger"),r.prototype.connectedCallback.call(this),this.bindEvents(),this.updateUserProfile()},y.prototype.disconnectedCallback=function(){this.unbindEvents(),r.prototype.disconnectedCallback.call(this)},y.prototype.bindEvents=function(){this.$logoutTrigger.addEventListener("click",this.logout),window.addEventListener(a.b,this.updateUserProfile),window.addEventListener(a.c,this.updateUserProfile)},y.prototype.unbindEvents=function(){this.$logoutTrigger.removeEventListener("click",this.logout),window.removeEventListener(a.b,this.updateUserProfile),window.removeEventListener(a.c,this.updateUserProfile)},Object.defineProperty(y.prototype,"$avatar",{get:function(){return this.querySelector("hpe-avatar")},enumerable:!1,configurable:!0}),Object.defineProperty(y.prototype,"$name",{get:function(){return this.querySelector(".gn-user-name")},enumerable:!1,configurable:!0}),Object.defineProperty(y.prototype,"$email",{get:function(){return this.querySelector(".gn-user-email")},enumerable:!1,configurable:!0}),Object.defineProperty(y.prototype,"$flyouts",{get:function(){return Array.from(document.body.querySelectorAll("gn-flyout"))},enumerable:!1,configurable:!0}),y.prototype.updateUserProfile=function(){var e=this;this._apiReady.then(function(){return e._api.auth.isUserLogged()}).then(function(t){e._setUserProfile(t.name,t.email)}).catch(function(){e._setUserProfile()})},y.prototype.logout=function(){var e=this;this._apiReady.then(function(){return e._api.auth.isUserLogged()}).then(function(t){t&&(Object(s.debug)("LOGOUT: ".concat(t.providers.join(","))),e._api.auth.logout(t.providers).then(function(){u.MetricsMyAccount.unlockSignInSuccessMutex(),e._setUserProfile(),Object(l.isAEM)()||e._reload()}))})},y.prototype._setUserProfile=function(t,e){this.$avatar.setAttribute("username",t||e||""),this.$name.textContent=t||e||"",this.$email.textContent=e||"",this.$flyouts.forEach(function(t){return t.hide()})},y.prototype._reload=function(){setTimeout(function(){return window.location.reload()},999)},y.is="gn-flyout-logout",o([i.a],y.prototype,"updateUserProfile",null),o([i.a],y.prototype,"logout",null),y);function y(){var e=r.call(this)||this;return e._apiReady=p.SharedAPI.cockpit$.then(function(t){return e._api=t}),e}},"hpe-gn/flyout/gn-flyout-trigger-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return l});var n,r,i=o(112),c=o(2),a=o(10),s=o(1),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},l=(r=i.a,e(u,r),Object.defineProperty(u.prototype,"$arrow",{get:function(){var t=document.createElement("span");return t.classList.add("gn-flyout-arrow"),t},enumerable:!1,configurable:!0}),u.prototype.connectedCallback=function(){r.prototype.connectedCallback.call(this),this.arrowDisabled||this.appendChild(this.$arrow)},u.prototype.disconnectedCallback=function(){r.prototype.disconnectedCallback.call(this),this.arrowDisabled||this.removeChild(this.$arrow)},u.is="gn-flyout-trigger",o([Object(a.a)({readonly:!0})],u.prototype,"arrowDisabled",void 0),o([Object(s.a)({defaultValue:"@+LG"})],u.prototype,"trackHover",void 0),o([Object(s.a)({defaultValue:"200"})],u.prototype,"hoverHideDelay",void 0),o([Object(c.a)()],u.prototype,"$arrow",null),u);function u(){return null!==r&&r.apply(this,arguments)||this}},"hpe-gn/flyout/gn-flyout-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return p});var n,r,i=o(1),c=o(46),a=o(4),s=o(119),l=o(2),u=o(40),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},p=(r=u.a,e(f,r),Object.defineProperty(f.prototype,"$focusableElements",{get:function(){return Array.from(this.querySelectorAll("a[href], button, [tabindex]"))},enumerable:!1,configurable:!0}),f.prototype.isItemFocusable=function(t){var e=t.closest("li");return"none"!==getComputedStyle(e||t).display},Object.defineProperty(f.prototype,"$boundaryFocusable",{get:function(){var t=this.$focusableElements.filter(this.isItemFocusable,this);return{first:t[0],last:t.pop()}},enumerable:!1,configurable:!0}),f.prototype.connectedCallback=function(){r.prototype.connectedCallback.call(this)},f.prototype.onShow=function(t){var e=this;r.prototype.onShow.call(this,t),setTimeout(function(){var t;return null===(t=e.$boundaryFocusable.first)||void 0===t?void 0:t.focus({preventScroll:!0})},f.animationTime)},f.prototype.onHide=function(t){var e=this;r.prototype.onHide.call(this,t),setTimeout(function(){var t;return null===(t=e.activator)||void 0===t?void 0:t.focus({preventScroll:!0})},f.animationTime)},f.prototype._onKeyboardEvent=function(t){if(this.open&&t.key===a.TAB){var e=this.$boundaryFocusable;return Object(s.b)(t,e.first,e.last)}return r.prototype._onKeyboardEvent.call(this,t)},f.is="gn-flyout",f.animationTime=450,o([Object(c.a)()],f.prototype,"activeClass",void 0),o([Object(c.a)()],f.prototype,"groupName",void 0),o([Object(c.a)()],f.prototype,"closeTrigger",void 0),o([Object(c.a)()],f.prototype,"closeOnEsc",void 0),o([Object(c.a)()],f.prototype,"closeOnOutsideAction",void 0),o([Object(i.a)({defaultValue:"gn-flyout-opened"})],f.prototype,"bodyClass",void 0),o([Object(c.a)()],f.prototype,"trackHoverParams",void 0),o([Object(l.a)()],f.prototype,"$focusableElements",null),f);function f(){var t=null!==r&&r.apply(this,arguments)||this;return t.activeClass="open",t.groupName="gn-flyout-group",t.closeTrigger=".gn-flyout-close",t.closeOnEsc=!0,t.closeOnOutsideAction=!0,t.trackHoverParams={hideDelay:200},t}},"hpe-gn/gn-header-v4":function(t,e,o){"use strict";o.r(e),o.d(e,"GNHeaderV4",function(){return j});var n,r,i=o("core/helpers/aem"),c=o(1),a=o(10),s=o(21),l=o("hpe-gn/search/gn-search-v4"),u=o("hpe-gn/secondary/gn-secondary-flyout-v4"),p=o("hpe-gn/primary/gn-mobile-v4"),f=o("hpe-gn/flyout/gn-flyout-trigger-v4"),y=o("hpe-gn/flyout/gn-flyout-logout-v4"),d=o("hpe-gn/flyout/gn-flyout-v4"),h=o("hpe-gn/primary/gn-user-profile-v4"),b=o(5),g=o(30),v=o(2),m=o("hpe-gn/flyout-primary/gn-flyout-primary-v4"),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},O=function(t,e){var o="function"==typeof Symbol&&t[Symbol.iterator];if(!o)return t;var n,r,i=o.call(t),c=[];try{for(;(void 0===e||0<e--)&&!(n=i.next()).done;)c.push(n.value)}catch(t){r={error:t}}finally{try{n&&!n.done&&(o=i.return)&&o.call(i)}finally{if(r)throw r.error}}return c},j=(r=s.a,e(_,r),Object.defineProperty(_,"observedAttributes",{get:function(){return["sticky"]},enumerable:!1,configurable:!0}),_.prototype.connectedCallback=function(){this.registerSubcomponents(),b.a.add(document.body,this.bodyClass),r.prototype.connectedCallback.call(this),!Object(i.isAEMAuthorMode)()&&this.sticky&&this.stickyObserver.observe(this)},_.prototype.disconnectedCallback=function(){v.a.has(this,"stickyObserver")&&this.stickyObserver.unobserve(this),b.a.remove(document.body,this.bodyClass),r.prototype.disconnectedCallback.call(this)},_.prototype.registerSubcomponents=function(){p.a.register(),l.a.register(),f.a.register(),y.a.register(),d.a.register(),m.a.register(),h.a.register(),u.a.register()},_.prototype.attributeChangedCallback=function(t,e,o){this.connected&&!Object(i.isAEMAuthorMode)()&&this.sticky&&this.stickyObserver.observe(this)},Object.defineProperty(_.prototype,"stickyObserver",{get:function(){var e=this;return new IntersectionObserver(function(t){t=O(t,1)[0];e.classList.toggle("gn-sticky",t.intersectionRatio<.995&&e.sticky)},{threshold:[.99,1],rootMargin:"".concat(this.hasSecondary?"67px":"1px"," 0px 0px 0px")})},enumerable:!1,configurable:!0}),Object.defineProperty(_.prototype,"theme",{get:function(){return this.classList.contains("dark-theme")?"dark":"light"},set:function(t){this.classList.toggle("dark-theme","dark"===t),this.classList.toggle("light-theme","light"===t)},enumerable:!1,configurable:!0}),_.is="gn-header",o([Object(c.a)({defaultValue:"gn-v4-active"})],_.prototype,"bodyClass",void 0),o([Object(a.a)()],_.prototype,"sticky",void 0),o([Object(a.a)({readonly:!0})],_.prototype,"hasSecondary",void 0),o([Object(a.a)({readonly:!0})],_.prototype,"hasSecondaryCta",void 0),o([g.a],_.prototype,"connectedCallback",null),o([Object(v.a)()],_.prototype,"stickyObserver",null),_);function _(){return null!==r&&r.apply(this,arguments)||this}j.register()},"hpe-gn/primary/gn-mobile-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return b});var n,r,i=o(4),c=o(0),a=o(30),s=o(46),l=o(2),u=o(119),p=o(73),f=o(25),y=o(5),d=o("hpe-gn/search/gn-search-v4"),h=o(40),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},b=(r=h.a,e(g,r),Object.defineProperty(g.prototype,"$focusableElements",{get:function(){return Array.from(this.querySelectorAll("a[href], button, [tabindex]")).reverse()},enumerable:!1,configurable:!0}),Object.defineProperty(g.prototype,"$lastFocusable",{get:function(){return this.$focusableElements.find(function(t){t=t.closest("li");return t&&"none"!==getComputedStyle(t).display})},enumerable:!1,configurable:!0}),g.prototype.connectedCallback=function(){this.$search=f.a.first(this.searchSel,this),r.prototype.connectedCallback.call(this),this.$search.addEventListener("esl:hide",this.onSearchHide),this.$search.addEventListener("keyup",this._onKeyboardEvent)},g.prototype.disconnectedCallback=function(){r.prototype.disconnectedCallback.call(this),this.$search.removeEventListener("esl:hide",this.onSearchHide),this.$search.removeEventListener("keyup",this._onKeyboardEvent)},g.prototype.onShow=function(t){r.prototype.onShow.call(this,t),this.$search.show({initiator:"mobile-menu",activator:this,blockScroll:!1,disableFocusTrap:!0}),p.a.requestLock(this,"none")},g.prototype.onHide=function(t){var e=this;y.a.remove(this,this.activeClass),"init"!==t.initiator&&"flyout-primary"!==t.initiator&&this.$search.hide({initiator:"mobile-menu",activator:this}),setTimeout(function(){return y.a.remove(document.body,e.bodyClass,e)},d.a.animationTime),p.a.requestUnlock(this,"none"),this.updateA11y()},g.prototype.focus=function(t){var e;if(this.open)return r.prototype.focus.call(this,t);null!==(e=this.activator)&&void 0!==e&&e.focus(t)},g.prototype._onKeyboardEvent=function(t){if(t.target&&this.contains(t.target)&&r.prototype._onKeyboardEvent.call(this,t),t.key===i.TAB&&this.open)return Object(u.b)(t,this.$search.$input,this.$lastFocusable)},g.prototype.onSearchHide=function(){this.hide()},g.is="gn-header-mobile",o([Object(s.a)()],g.prototype,"activeClass",void 0),o([Object(s.a)()],g.prototype,"bodyClass",void 0),o([Object(s.a)()],g.prototype,"closeOnEsc",void 0),o([Object(s.a)({value:"::parent(gn-header)::find(gn-header-search)"})],g.prototype,"searchSel",void 0),o([Object(l.a)()],g.prototype,"$focusableElements",null),o([a.a],g.prototype,"connectedCallback",null),o([c.a],g.prototype,"_onKeyboardEvent",null),o([c.a],g.prototype,"onSearchHide",null),g);function g(){var t=null!==r&&r.apply(this,arguments)||this;return t.activeClass="open",t.bodyClass="gn-primary-mobile-opened",t.closeOnEsc=!0,t}},"hpe-gn/primary/gn-user-profile-v4":function(t,e,o){"use strict";o.d(e,"b",function(){return u}),o.d(e,"c",function(){return p}),o.d(e,"a",function(){return f});var n,r,i=o(21),c=o(0),a=o("core/log"),s=o("core/helpers/metrics-my-account"),l=o("cockpit/api/shared"),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},u="auth:api:login",p="auth:api:logout",f=(r=i.a,e(y,r),y.prototype.connectedCallback=function(){r.prototype.connectedCallback.call(this),this.updateUserProfile(),this.bindEvents()},y.prototype.disconnectedCallback=function(){r.prototype.disconnectedCallback.call(this),this.unbindEvents()},y.prototype.bindEvents=function(){window.addEventListener(u,this.updateUserProfile),window.addEventListener(p,this.updateUserProfile)},y.prototype.unbindEvents=function(){window.removeEventListener(u,this.updateUserProfile),window.removeEventListener(p,this.updateUserProfile)},Object.defineProperty(y.prototype,"$avatar",{get:function(){return this.querySelector("hpe-avatar")},enumerable:!1,configurable:!0}),y.prototype.updateUserProfile=function(){var e=this;this._apiReady.then(function(){return e._api.auth.isUserLogged()}).then(function(t){Object(a.debug)("LOGIN: getUserInfo",t),e.$avatar.setAttribute("username",t.name||t.email||""),s.MetricsMyAccount.trackSignInSuccess(t.email,t.providers)}).catch(function(){Object(a.debug)("LOGIN: getUserInfo none"),e.$avatar.setAttribute("username","")})},y.is="gn-user-profile",o([c.a],y.prototype,"updateUserProfile",null),y);function y(){var e=r.call(this)||this;return e._apiReady=l.SharedAPI.cockpit$.then(function(t){return e._api=t}),e}},"hpe-gn/search/gn-search-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return y});var n,r,i=o(1),c=o(46),a=o(4),s=o(119),l=o(0),u=o(73),p=o(33),f=o(40),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},y=(r=f.a,e(d,r),Object.defineProperty(d.prototype,"$form",{get:function(){return this.querySelector("form")},enumerable:!1,configurable:!0}),Object.defineProperty(d.prototype,"$input",{get:function(){return this.querySelector("input")},enumerable:!1,configurable:!0}),Object.defineProperty(d.prototype,"$closeBtn",{get:function(){return this.querySelector(this.closeTrigger)},enumerable:!1,configurable:!0}),d.prototype.connectedCallback=function(){r.prototype.connectedCallback.call(this),this.closeConditionQuery=p.a.for(this.closeCondition),this.closeConditionQuery.addListener(this.onCloseQueryChange)},d.prototype.disconnectedCallback=function(){r.prototype.disconnectedCallback.call(this),this.closeConditionQuery.removeListener(this.onCloseQueryChange)},d.prototype.onShow=function(t){this.disableFocusTrap=t.disableFocusTrap,r.prototype.onShow.call(this,t),setTimeout(this.postShow.bind(this,t),d.animationTime)},d.prototype.postShow=function(t){this.$input.focus({preventScroll:!0}),t.blockScroll&&u.a.requestLock(this,"pseudo")},d.prototype.onHide=function(t){this.disableFocusTrap=!1,r.prototype.onHide.call(this,t),setTimeout(this.postHide.bind(this,t),d.animationTime)},d.prototype.postHide=function(t){var e=this;t.blockScroll&&u.a.requestUnlock(this,"pseudo"),setTimeout(function(){var t;e.$form.reset(),null!==(t=e.activator)&&void 0!==t&&t.focus({preventScroll:!0})},50)},d.prototype._onKeyboardEvent=function(t){return this.open&&t.key===a.TAB&&!this.disableFocusTrap?Object(s.b)(t,this.$input,this.$closeBtn):r.prototype._onKeyboardEvent.call(this,t)},d.prototype.onCloseQueryChange=function(){this.closeConditionQuery.matches&&this.hide()},d.prototype._onOutsideAction=function(t){t.target.closest(this.ignoredSiblings)||r.prototype._onOutsideAction.call(this,t)},d.is="gn-header-search",d.animationTime=450,o([Object(i.a)({defaultValue:"@+LG"})],d.prototype,"closeCondition",void 0),o([Object(i.a)({defaultValue:"gn-flyout-primary, gn-header-mobile"})],d.prototype,"ignoredSiblings",void 0),o([Object(c.a)()],d.prototype,"activeClass",void 0),o([Object(c.a)()],d.prototype,"bodyClass",void 0),o([Object(c.a)()],d.prototype,"closeTrigger",void 0),o([Object(c.a)()],d.prototype,"closeOnEsc",void 0),o([Object(c.a)()],d.prototype,"closeOnOutsideAction",void 0),o([Object(c.a)()],d.prototype,"defaultParams",void 0),o([l.a],d.prototype,"onCloseQueryChange",null),o([l.a],d.prototype,"_onOutsideAction",null),d);function d(){var t=null!==r&&r.apply(this,arguments)||this;return t.activeClass="open",t.bodyClass="gn-search-opened",t.closeTrigger=".gn-search-close",t.closeOnEsc=!0,t.closeOnOutsideAction=!0,t.defaultParams={blockScroll:!0},t.disableFocusTrap=!1,t}},"hpe-gn/secondary/gn-secondary-flyout-v4":function(t,e,o){"use strict";o.d(e,"a",function(){return a});var n,r,i=o(46),c=o("hpe-gn/flyout/gn-flyout-v4"),e=(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),o=function(t,e,o,n){var r,i=arguments.length,c=i<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,o):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,o,n);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,o,c):r(e,o))||c);return 3<i&&c&&Object.defineProperty(e,o,c),c},a=(r=c.a,e(s,r),s.is="gn-secondary-flyout",o([Object(i.a)()],s.prototype,"groupName",void 0),o([Object(i.a)()],s.prototype,"bodyClass",void 0),s);function s(){var t=null!==r&&r.apply(this,arguments)||this;return t.groupName="gn-secondary-flyout-group",t.bodyClass="gn-secondary-flyout-opened",t}}}]);