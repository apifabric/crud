import { MenuRootItem } from 'ontimize-web-ngx';

import { AccountCardComponent } from './Account-card/Account-card.component';

import { CompanyCardComponent } from './Company-card/Company-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { CustomerHistoryCardComponent } from './CustomerHistory-card/CustomerHistory-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplyCardComponent } from './Supply-card/Supply-card.component';

import { TransactionCardComponent } from './Transaction-card/Transaction-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Account', name: 'ACCOUNT', icon: 'view_list', route: '/main/Account' }
    
        ,{ id: 'Company', name: 'COMPANY', icon: 'view_list', route: '/main/Company' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'CustomerHistory', name: 'CUSTOMERHISTORY', icon: 'view_list', route: '/main/CustomerHistory' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'Supply', name: 'SUPPLY', icon: 'view_list', route: '/main/Supply' }
    
        ,{ id: 'Transaction', name: 'TRANSACTION', icon: 'view_list', route: '/main/Transaction' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AccountCardComponent

    ,CompanyCardComponent

    ,CustomerCardComponent

    ,CustomerHistoryCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PaymentCardComponent

    ,ProductCardComponent

    ,SupplierCardComponent

    ,SupplyCardComponent

    ,TransactionCardComponent

];